from fastapi import FastAPI
from ingest_data.seedwork.infraestructura.utils import time_millis
from orquestador_saga.api import v1
from orquestador_saga.aplicacion.comandos.ingesta_datos import ComandoIniciarCargaDatos
from orquestador_saga.config.api import app_configs, settings
from orquestador_saga.api.v1.router import router as v1

from orquestador_saga.infraestructura.consumidores import suscribirse_a_topico
from orquestador_saga.infraestructura.v1.eventos import EventoCargaFinalizada, CargaFinalizada, EventoCargaFallida, CargaFallida
from orquestador_saga.infraestructura.v1.eventos import EventoProcesamientoDatosFinalizado, EventoProcesamientoDatosFallido, ProcesamientoDatosFinalizado, ProcesamientoDatosFallido
from orquestador_saga.infraestructura.v1.eventos import EventoValidacionFinalizada, EventoValidacionFallido, ValidacionFinalizada, ValidacionFallido
from orquestador_saga.infraestructura.v1.eventos import EventoQueryEntrenamiendoFinalizado, EventoQueryEntrenamiendoFallido, QueryEntrenamiendoFinalizado, QueryEntrenamiendoFallido

from orquestador_saga.seedwork.infraestructura import utils

import asyncio
import time
import traceback
from processed_data.modulos.infraestructura.despachadores import Despachador
import uvicorn


app = FastAPI(**app_configs)
tasks = list()

@app.on_event("startup")
async def app_startup():
    global tasks
    task1 = asyncio.ensure_future(suscribirse_a_topico("evento-ingesta-datos-finalizado", "sub-ingest-data", EventoCargaFinalizada))
    task2 = asyncio.ensure_future(suscribirse_a_topico("evento-procesar-datos-finalizado", "sub-processed-data", EventoProcesamientoDatosFinalizado))
    task3 = asyncio.ensure_future(suscribirse_a_topico("evento-validacion-finalizada", "sub-validacion", EventoValidacionFinalizada))
    task4 = asyncio.ensure_future(suscribirse_a_topico("evento-query-entrenamiento-finalizado", "sub-query-entrenamiento", EventoQueryEntrenamiendoFinalizado))
    task5 = asyncio.ensure_future(suscribirse_a_topico("evento-ingesta-datos-fallido", "sub-ingest-data", EventoCargaFallida))
    task6 = asyncio.ensure_future(suscribirse_a_topico("evento-procesar-datos-fallido", "sub-processed-data", EventoProcesamientoDatosFallido))
    task7 = asyncio.ensure_future(suscribirse_a_topico("evento-validacion-fallido", "sub-validacion", EventoValidacionFallido))
    task8 = asyncio.ensure_future(suscribirse_a_topico("evento-query-entrenamiento-fallido", "sub-query-entrenamiento", EventoQueryEntrenamiendoFallido))

    tasks.append(task1)
    tasks.append(task2)
    tasks.append(task3)
    tasks.append(task4)
    tasks.append(task5)
    tasks.append(task6)
    tasks.append(task7)
    tasks.append(task8)

@app.on_event("shutdown")
def shutdown_event():
    global tasks
    for task in tasks:
        task.cancel()
        
@app.get("/prueba-evento-ingesta-datos-finalizado", include_in_schema=False)
async def prueba_evento_ingesta_datos_finalizado() -> dict[str, str]:
    payload = CargaFinalizada(
        traceId="123456",
        partner_id="partner1",
        user_id="user1",
        url_raw_data="http://example.com/data1",
        url_s3="s3://bucket/data1"
    )
    
    evento = EventoCargaFinalizada(
        id="1232321321", 
        time=time_millis(), 
        ingestion=time_millis(),
        specversion="1.0",
        type="evento-ingesta-datos-finalizado",
        datacontenttype=CargaFinalizada.__name__,
        service_name="ingesta-servicio",
        data=payload
    )
    
    despachador = Despachador()
    despachador.publicar_mensaje(evento, "evento-ingesta-datos-finalizado")
    
    return {"status": "ok"}

@app.get("/prueba-evento-procesar-datos-finalizado", include_in_schema=False)
async def prueba_evento_procesar_datos_finalizado() -> dict[str, str]:
    payload = ProcesamientoDatosFinalizado(
        traceId="654321",
        partner_id="partner2",
        user_id="user2",
        url_raw_data="http://example.com/data2",
        url_s3="s3://bucket/data2",
        path="/processed/path"
    )
    
    evento = EventoProcesamientoDatosFinalizado(
        id="1232321322", 
        time=time_millis(), 
        ingestion=time_millis(),
        specversion="1.0",
        type="evento-procesar-datos-finalizado",
        datacontenttype=ProcesamientoDatosFinalizado.__name__,
        service_name="procesamiento-servicio",
        data=payload
    )
    
    despachador = Despachador()
    despachador.publicar_mensaje(evento, "evento-procesar-datos-finalizado")
    
    return {"status": "ok"}

@app.get("/prueba-evento-validacion-finalizada", include_in_schema=False)
async def prueba_evento_validacion_finalizada() -> dict[str, str]:
    payload = ValidacionFinalizada(
        traceId="789012",
        partner_id="partner3",
        user_id="user3",
        url_raw_data="http://example.com/data3",
        url_s3="s3://bucket/data3",
        path="/validacion/path",
        es_valido=True
    )
    
    evento = EventoValidacionFinalizada(
        id="1232321323", 
        time=time_millis(), 
        ingestion=time_millis(),
        specversion="1.0",
        type="evento-validacion-finalizada",
        datacontenttype=ValidacionFinalizada.__name__,
        service_name="validacion-servicio",
        data=payload
    )
    
    despachador = Despachador()
    despachador.publicar_mensaje(evento, "evento-validacion-finalizada")
    
    return {"status": "ok"}

@app.get("/prueba-evento-query-entrenamiento-finalizado", include_in_schema=False)
async def prueba_evento_query_entrenamiento_finalizado() -> dict[str, str]:
    payload = QueryEntrenamiendoFinalizado(
        traceId="234567",
        partner_id="partner4",
        user_id="user4",
        url_raw_data="http://example.com/data4",
        url_s3="s3://bucket/data4",
        path="/query/path",
        es_valido=True,
        entrenamiendo_completado=True
    )
    
    evento = EventoQueryEntrenamiendoFinalizado(
        id="1232321324", 
        time=time_millis(), 
        ingestion=time_millis(),
        specversion="1.0",
        type="evento-query-entrenamiento-finalizado",
        datacontenttype=QueryEntrenamiendoFinalizado.__name__,
        service_name="entrenamiento-servicio",
        data=payload
    )
    
    despachador = Despachador()
    despachador.publicar_mensaje(evento, "evento-query-entrenamiento-finalizado")
    
    return {"status": "ok"}

@app.get("/prueba-evento-ingesta-datos-fallido", include_in_schema=False)
async def prueba_evento_ingesta_datos_fallido() -> dict[str, str]:
    payload = CargaFallida(
        traceId="987654",
        partner_id="partner5",
        user_id="user5",
        url_raw_data="http://example.com/data5"
    )
    
    evento = EventoCargaFallida(
        id="1232321325", 
        time=time_millis(), 
        ingestion=time_millis(),
        specversion="1.0",
        type="evento-ingesta-datos-fallido",
        datacontenttype=CargaFallida.__name__,
        service_name="ingesta-servicio",
        data=payload
    )
    
    despachador = Despachador()
    despachador.publicar_mensaje(evento, "evento-ingesta-datos-fallido")
    
    return {"status": "ok"}

@app.get("/prueba-evento-procesar-datos-fallido", include_in_schema=False)
async def prueba_evento_procesar_datos_fallido() -> dict[str, str]:
    payload = ProcesamientoDatosFallido(
        traceId="876543",
        partner_id="partner6",
        user_id="user6",
        url_raw_data="http://example.com/data6",
        url_s3="s3://bucket/data6"
    )
    
    evento = EventoProcesamientoDatosFallido(
        id="1232321326", 
        time=time_millis(), 
        ingestion=time_millis(),
        specversion="1.0",
        type="evento-procesar-datos-fallido",
        datacontenttype=ProcesamientoDatosFallido.__name__,
        service_name="procesamiento-servicio",
        data=payload
    )
    
    despachador = Despachador()
    despachador.publicar_mensaje(evento, "evento-procesar-datos-fallido")
    
    return {"status": "ok"}

@app.get("/prueba-evento-validacion-fallido", include_in_schema=False)
async def prueba_evento_validacion_fallido() -> dict[str, str]:
    payload = ValidacionFallido(
        traceId="765432",
        partner_id="partner7",
        user_id="user7",
        url_raw_data="http://example.com/data7",
        url_s3="s3://bucket/data7",
        path="/validacion/fallida"
    )
    
    evento = EventoValidacionFallido(
        id="1232321327", 
        time=time_millis(), 
        ingestion=time_millis(),
        specversion="1.0",
        type="evento-validacion-fallido",
        datacontenttype=ValidacionFallido.__name__,
        service_name="validacion-servicio",
        data=payload
    )
    
    despachador = Despachador()
    despachador.publicar_mensaje(evento, "evento-validacion-fallido")
    
    return {"status": "ok"}

@app.get("/prueba-evento-query-entrenamiento-fallido", include_in_schema=False)
async def prueba_evento_query_entrenamiento_fallido() -> dict[str, str]:
    payload = QueryEntrenamiendoFallido(
        traceId="654321",
        partner_id="partner8",
        user_id="user8",
        url_raw_data="http://example.com/data8",
        url_s3="s3://bucket/data8",
        path="/query/fallido",
        es_valido=False
    )
    
    evento = EventoQueryEntrenamiendoFallido(
        id="1232321328", 
        time=time_millis(), 
        ingestion=time_millis(),
        specversion="1.0",
        type="evento-query-entrenamiento-fallido",
        datacontenttype=QueryEntrenamiendoFallido.__name__,
        service_name="entrenamiento-servicio",
        data=payload
    )
    
    despachador = Despachador()
    despachador.publicar_mensaje(evento, "evento-query-entrenamiento-fallido")
    
    return {"status": "ok"}


@app.get("/health", include_in_schema=False)
async def health() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(v1, prefix="/v1", tags=["Version 1"])
