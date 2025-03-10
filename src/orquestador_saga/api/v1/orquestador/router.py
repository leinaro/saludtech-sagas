from fastapi import APIRouter, status, BackgroundTasks
from orquestador_saga.aplicacion.comandos.processed_data import ComandoIniciarProcesamientoDatos
from orquestador_saga.seedwork.presentacion.dto import RespuestaAsincrona
from orquestador_saga.seedwork.aplicacion.comandos import ejecutar_commando
from orquestador_saga.seedwork.aplicacion.queries import ejecutar_query

from .dto import ProcesarDatos


router = APIRouter()

@router.post("/orquestador", status_code=status.HTTP_202_ACCEPTED, response_model=RespuestaAsincrona)
async def procesar_datos(procesar_datos: ProcesarDatos, background_tasks: BackgroundTasks) -> dict[str, str]:
    comando = ComandoIniciarProcesamientoDatos(
        partner_id=procesar_datos.partner_id,
        user_id = procesar_datos.user_id,
        url_raw_data = procesar_datos.url_raw_data,
        #tipo_processed_data = procesar_datos.tipo_processed_data,
    )
    background_tasks.add_task(ejecutar_commando, comando)
    return RespuestaAsincrona(mensaje="Orquestador....")