from fastapi import FastAPI
from orquestador_saga.api import v1
from orquestador_saga.aplicacion.comandos.ingesta_datos import ComandoIniciarCargarDatos
from orquestador_saga.config.api import app_configs, settings
from orquestador_saga.api.v1.router import router as v1

#from orquestador_saga.dominio.eventos.processed_data import EventoDatosGuardados
#from orquestador_saga.dominio.eventos.query_entrenamiento import EventoQueryEntrenamiendoFinalizado
#from orquestador_saga.dominio.eventos.validacion import EventoValidacionFinalizada
from orquestador_saga.infraestructura.consumidores import suscribirse_a_topico
from orquestador_saga.infraestructura.v1.eventos import EventoCargaFinalizada, EventoDatoProcesado, EventoDatosGuardados, EventoValidacionFinalizada, EventoQueryEntrenamiendoFinalizado
from orquestador_saga.seedwork.infraestructura import utils

import asyncio
import time
import traceback
import uvicorn


app = FastAPI(**app_configs)
tasks = list()

@app.on_event("startup")
async def app_startup():
    global tasks
  #  task1 = asyncio.ensure_future(suscribirse_a_topico("evento-ingesta-datos", "sub-ingest-data", EventoCargaFinalizada))
    task2 = asyncio.ensure_future(suscribirse_a_topico("evento-procesar-datos", "sub-processed-data", EventoDatoProcesado))
  #  task3 = asyncio.ensure_future(suscribirse_a_topico("evento-validar", "sub-validar", EventoValidacionFinalizada))
  #  task4 = asyncio.ensure_future(suscribirse_a_topico("evento-query-entrenamiento", "sub-query-entrenamiento", EventoQueryEntrenamiendoFinalizado))

   # tasks.append(task1)
    tasks.append(task2)
    #tasks.append(task3)
    #tasks.append(task4)

@app.on_event("shutdown")
def shutdown_event():
    global tasks
    for task in tasks:
        task.cancel()

@app.get("/health", include_in_schema=False)
async def health() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(v1, prefix="/v1", tags=["Version 1"])
