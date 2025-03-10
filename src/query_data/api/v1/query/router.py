from fastapi import APIRouter, status, BackgroundTasks
from .dto import ProcesarDatos
from .responses import RespuestaAsincrona
from .commands import ComandoIniciarProcesamientoDatos, ejecutar_commando

router = APIRouter()

@router.post("/query", status_code=status.HTTP_202_ACCEPTED, response_model=RespuestaAsincrona)
async def procesar_datos(procesar_datos: ProcesarDatos, background_tasks: BackgroundTasks) -> dict[str, str]:
    comando = ComandoIniciarProcesamientoDatos(
        nombres=procesar_datos.url_raw_data,
    )
    background_tasks.add_task(ejecutar_commando, comando)
    return RespuestaAsincrona(mensaje="Procesando datos")