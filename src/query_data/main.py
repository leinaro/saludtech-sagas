from fastapi import FastAPI
from query_data.config.api import app_configs, settings
from query_data.api.v1.router import router as v1
from query_data.modulos.infraestructura.consumidores import suscribirse_a_topico
from query_data.modulos.infraestructura.v1.eventos import EventoQueryEntrenamientoFinalizado, EventoQueryEntrenamiendoFallido
from query_data.modulos.infraestructura.v1.comandos import ComandoIniciarQueryEntrenamiento, ComandoCancelarQueryEntrenamiento
from query_data.modulos.infraestructura.despachadores import Despachador
from query_data.seedwork.infraestructura import utils

import asyncio
import time
import traceback
import uvicorn

app = FastAPI(**app_configs)
tasks = list()

@app.on_event("startup")
async def app_startup():
    global tasks
    #task1 = asyncio.ensure_future(suscribirse_a_topico("evento-query-entrenamiento", "sub-query", EventoQueryEntrenamientoFinalizado))
    task2 = asyncio.ensure_future(suscribirse_a_topico("comando-iniciar-query-entrenamiento", "sub-com-iniciar-query", ComandoIniciarQueryEntrenamiento))
    task3 = asyncio.ensure_future(suscribirse_a_topico("comando-cancelar-query-entrenamiento", "sub-com-cancelar-query", ComandoCancelarQueryEntrenamiento))
    #tasks.append(task1)
    tasks.append(task2)
    tasks.append(task3)

@app.on_event("shutdown")
def shutdown_event():
    global tasks
    for task in tasks:
        task.cancel()

@app.get("/query/iniciar-entrenamiento", include_in_schema=False)
async def query_iniciar_entrenamiento() -> dict[str, str]:
    payload = ComandoIniciarQueryEntrenamiento(
        partner_id="partner123",
        user_id="user123",
        url_raw_data="http://example.com/data"
    )

    comando = ComandoIniciarQueryEntrenamiento(
        partner_id=payload.partner_id,
        user_id=payload.user_id,
        url_raw_data=payload.url_raw_data
    )
    despachador = Despachador()
    despachador.publicar_mensaje(comando, "comando-iniciar-query-entrenamiento")
    return {"status": "ok"}

@app.get("/query/cancelar-entrenamiento", include_in_schema=False)
async def query_cancelar_entrenamiento() -> dict[str, str]:
    payload = ComandoCancelarQueryEntrenamiento(
        partner_id="partner123",
        user_id="user123",
        url_raw_data="http://example.com/data"
    )

    comando = ComandoCancelarQueryEntrenamiento(
        partner_id=payload.partner_id,
        user_id=payload.user_id,
        url_raw_data=payload.url_raw_data
    )
    despachador = Despachador()
    despachador.publicar_mensaje(comando, "comando-cancelar-query-entrenamiento")
    return {"status": "ok"}

@app.get("/health", include_in_schema=False)
async def health() -> dict[str, str]:
    return {"status": "ok"}

@app.get("/")
def read_root():
    return {"message": "Welcome to the Query Data API"}

app.include_router(v1, prefix="/v1", tags=["Version 1"])
