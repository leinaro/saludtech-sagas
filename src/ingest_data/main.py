from fastapi import FastAPI
from ingest_data.config.api import app_configs, settings
from ingest_data.api.v1.router import router as v1

from ingest_data.modulos.infraestructura.consumidores import suscribirse_a_topico
from ingest_data.modulos.infraestructura.v1.eventos import DatoIngestado, EventoDatoIngestado, EventoIngestacionCancelada, EventoIngestacionFinalizada
from ingest_data.modulos.infraestructura.v1.comandos import ComandoIniciarIngestacion, ComandoIngestarDato, ComandoCancelarIngestacion, IniciarIngestacion, IngestarDato, CancelarIngestacion
from ingest_data.modulos.infraestructura.despachadores import Despachador
from ingest_data.seedwork.infraestructura import utils

import asyncio
import time
import traceback
import uvicorn


app = FastAPI(**app_configs)
tasks = list()

@app.on_event("startup")
async def app_startup():
    global tasks
    task1 = asyncio.ensure_future(suscribirse_a_topico("comando-iniciar-ingestacion", "sub-com-iniciar-ingestacion", ComandoIniciarIngestacion))
    task2 = asyncio.ensure_future(suscribirse_a_topico("comando-ingestar-dato", "sub-com-ingestar-dato", ComandoIngestarDato))
    task3 = asyncio.ensure_future(suscribirse_a_topico("comando-cancelar-ingestacion", "sub-com-cancelar-ingestacion", ComandoCancelarIngestacion))
    tasks.append(task1)
    tasks.append(task2)
    tasks.append(task3)

@app.on_event("shutdown")
def shutdown_event():
    global tasks
    for task in tasks:
        task.cancel()

@app.get("/prueba-ingestacion-iniciada", include_in_schema=False)
async def prueba_ingestacion_iniciada() -> dict[str, str]:
    payload = IniciarIngestacion(
        id = "1232321321", 
        fuente = "api_externa",
        fecha_inicio_ingestacion = utils.time_millis()
    )

    comando = ComandoIniciarIngestacion(
        time=utils.time_millis(),
        ingestion=utils.time_millis(),
        datacontenttype=IniciarIngestacion.__name__,
        data = payload
    )
    despachador = Despachador()
    despachador.publicar_mensaje(comando, "comando-iniciar-ingestacion")
    return {"status": "ok"}

@app.get("/prueba-ingestacion-cancelada", include_in_schema=False)
async def prueba_ingestacion_cancelada() -> dict[str, str]:
    payload = CancelarIngestacion(
        id = "1232321321", 
        fecha_cancelacion = utils.time_millis()
    )

    comando = ComandoCancelarIngestacion(
        time=utils.time_millis(),
        ingestion=utils.time_millis(),
        datacontenttype=CancelarIngestacion.__name__,
        data = payload
    )
    despachador = Despachador()
    despachador.publicar_mensaje(comando, "comando-cancelar-ingestacion")
    return {"status": "ok"}

@app.get("/prueba-dato-ingestado", include_in_schema=False)
async def prueba_dato_ingestado() -> dict[str, str]:
    payload = DatoIngestado(id = "1232321321", fuente = "api_externa", fecha_ingestacion = utils.time_millis())
    evento = EventoDatoIngestado(
        time=utils.time_millis(),
        ingestion=utils.time_millis(),
        datacontenttype=DatoIngestado.__name__,
        data = payload
    )
    despachador = Despachador()
    despachador.publicar_mensaje(evento, "evento-dato-ingestado")
    return {"status": "ok"}

@app.get("/prueba-ingestar-dato", include_in_schema=False)
async def prueba_ingestar_dato() -> dict[str, str]:
    payload = IngestarDato(
        id = "1232321321", 
        fuente = "api_externa",
        contenido = {"campo1": "valor1", "campo2": "valor2"},
        fecha_ingestacion = utils.time_millis()
    )

    comando = ComandoIngestarDato(
        time=utils.time_millis(),
        ingestion=utils.time_millis(),
        datacontenttype=IngestarDato.__name__,
        data = payload
    )
    despachador = Despachador()
    despachador.publicar_mensaje(comando, "comando-ingestar-dato")
    return {"status": "ok"}

@app.get("/prueba-ingestacion-finalizada", include_in_schema=False)
async def prueba_ingestacion_finalizada() -> dict[str, str]:
    payload = DatoIngestado(id = "1232321321", fuente = "api_externa", fecha_ingestacion = utils.time_millis())
    evento = EventoIngestacionFinalizada(
        time=utils.time_millis(),
        ingestion=utils.time_millis(),
        datacontenttype=DatoIngestado.__name__,
        data = payload
    )
    despachador = Despachador()
    despachador.publicar_mensaje(evento, "evento-ingestacion-finalizada")
    return {"status": "ok"}

@app.get("/health", include_in_schema=False)
async def health() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(v1, prefix="/v1", tags=["Version 1"]) 