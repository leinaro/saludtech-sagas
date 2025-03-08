from fastapi import FastAPI
from processed_data.config.api import app_configs, settings
from processed_data.api.v1.router import router as v1

from processed_data.modulos.infraestructura.consumidores import suscribirse_a_topico
from processed_data.modulos.infraestructura.v1.eventos import EventoDatoProcesado, DatoProcesadoGuardado, ProcesamientoDatosCancelado, ProcesamientoDatosIniciado, TipoDatos
from processed_data.modulos.infraestructura.v1.comandos import ComandoIniciarProcesamientoDatos, ComandoGuardarDatoProcesado, ComandoCancelarProcesamientoDatos, ProcesarDatos, GuardarDatoProcesado, CancelarProcesamientoDatos
from processed_data.modulos.infraestructura.v1 import TipoDatos
from processed_data.modulos.infraestructura.despachadores import Despachador
from processed_data.seedwork.infraestructura import utils

import asyncio
import time
import traceback
import uvicorn


app = FastAPI(**app_configs)
tasks = list()

@app.on_event("startup")
async def app_startup():
    global tasks
    task1 = asyncio.ensure_future(suscribirse_a_topico("evento-procesar-datos", "sub-processed-data", EventoDatoProcesado))
    task2 = asyncio.ensure_future(suscribirse_a_topico("comando-iniciar-procesamiento-datos", "sub-com-iniciar-procesamiento-datos", ComandoIniciarProcesamientoDatos))
    task3 = asyncio.ensure_future(suscribirse_a_topico("comando-guardar-datos-procesados", "sub-com-guardar-datos-procesados", ComandoGuardarDatoProcesado))
    task4 = asyncio.ensure_future(suscribirse_a_topico("comando-cancelar-procesamiento-datos", "sub-com-cancelar-procesamiento-datos", ComandoCancelarProcesamientoDatos))
    tasks.append(task1)
    tasks.append(task2)
    tasks.append(task3)
    tasks.append(task4)

@app.on_event("shutdown")
def shutdown_event():
    global tasks
    for task in tasks:
        task.cancel()

@app.get("/prueba-procesamiento-datos-iniciado", include_in_schema=False)
async def prueba_procesamiento_datos_iniciado() -> dict[str, str]:
    payload = ProcesamientoDatosIniciado(
        id = "1232321321", 
        partner_id = "1234567890",
        user_id = "0987654321",
        url_raw_data = "qwertyuio",
        tipo_processed_data = TipoDatos.imagen_medica,
        fecha_inicio = utils.time_millis())

    evento = EventoDatoProcesado(
        time=utils.time_millis(),
        ingestion=utils.time_millis(),
        datacontenttype=ProcesamientoDatosIniciado.__name__,
        procesamiento_datos_iniciado = payload
    )
    despachador = Despachador()
    despachador.publicar_mensaje(evento, "evento-procesar-datos")
    return {"status": "ok"}

@app.get("/prueba-procesamiento-datos-cancelado", include_in_schema=False)
async def prueba_procesamiento_datos_cancelado() -> dict[str, str]:
    payload = ProcesamientoDatosCancelado(id = "1232321321", fecha_cancelacion = utils.time_millis())
    evento = EventoDatoProcesado(
        time=utils.time_millis(),
        ingestion=utils.time_millis(),
        datacontenttype=ProcesamientoDatosCancelado.__name__,
        procesamiento_datos_cancelado = payload
    )
    despachador = Despachador()
    despachador.publicar_mensaje(evento, "evento-procesar-datos")
    return {"status": "ok"}

@app.get("/prueba-dato-procesado-guardado", include_in_schema=False)
async def prueba_guardar_dato_procesado() -> dict[str, str]:
    payload = DatoProcesadoGuardado(id = "1232321321", fecha_guardado = utils.time_millis())
    evento = EventoDatoProcesado(
        time=utils.time_millis(),
        ingestion=utils.time_millis(),
        datacontenttype=DatoProcesadoGuardado.__name__,
        dato_procesado_guardado = payload
    )
    despachador = Despachador()
    despachador.publicar_mensaje(evento, "evento-procesar-datos")
    return {"status": "ok"}

@app.get("/prueba-procesar-datos", include_in_schema=False)
async def prueba_procesar_datos() -> dict[str, str]:
    payload = ProcesarDatos(
        id = "1232321321", 
        partner_id = "1234567890",
        user_id = "0987654321",
        url_raw_data = "qwertyuio",
        tipo_processed_data = TipoDatos.imagen_medica,
        fecha_creacion = utils.time_millis()
    )

    comando = ComandoIniciarProcesamientoDatos(
        time=utils.time_millis(),
        ingestion=utils.time_millis(),
        datacontenttype=ProcesarDatos.__name__,
        data = payload
    )
    despachador = Despachador()
    despachador.publicar_mensaje(comando, "comando-iniciar-procesamiento-datos")
    return {"status": "ok"}

@app.get("/prueba-guardar-datos-procesados", include_in_schema=False)
async def prueba_guardar_datos_procesados() -> dict[str, str]:
    payload = GuardarDatoProcesado(
        id = "1232321321", 
        fecha_guardado = utils.time_millis()
    )

    comando = ComandoGuardarDatoProcesado(
        time=utils.time_millis(),
        ingestion=utils.time_millis(),
        datacontenttype=GuardarDatoProcesado.__name__,
        data = payload
    )
    despachador = Despachador()
    despachador.publicar_mensaje(comando, "comando-validar-usuario")
    return {"status": "ok"}

@app.get("/prueba-cancelar-procesar-datos", include_in_schema=False)
async def prueba_cancelar_procesar_datos() -> dict[str, str]:
    payload = CancelarProcesamientoDatos(
        id = "1232321321", 
        fecha_cancelacion = utils.time_millis()
    )

    comando = ComandoCancelarProcesamientoDatos(
        time=utils.time_millis(),
        ingestion=utils.time_millis(),
        datacontenttype=CancelarProcesamientoDatos.__name__,
        data = payload
    )
    despachador = Despachador()
    despachador.publicar_mensaje(comando, "comando-desactivar-usuario")
    return {"status": "ok"}

@app.get("/health", include_in_schema=False)
async def health() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(v1, prefix="/v1", tags=["Version 1"])
