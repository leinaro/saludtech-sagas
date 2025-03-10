from fastapi import APIRouter, status, BackgroundTasks
from validacion.modulos.aplicacion.comandos.registrar_usuario import ComandoRegistrarUsuario
from validacion.seedwork.presentacion.dto import RespuestaAsincrona
from validacion.seedwork.aplicacion.comandos import ejecutar_commando
from validacion.seedwork.aplicacion.queries import ejecutar_query

from .dto import RegistrarUsuario


router = APIRouter()

@router.post("/validar", status_code=status.HTTP_202_ACCEPTED, response_model=RespuestaAsincrona)
async def registrar_usuario(registrar_usuario: RegistrarUsuario, background_tasks: BackgroundTasks) -> dict[str, str]:
    comando = ComandoRegistrarUsuario(
        nombres=registrar_usuario.nombres,
        apellidos=registrar_usuario.apellidos,
        email=registrar_usuario.email,
        password=registrar_usuario.password,
        es_empresarial=registrar_usuario.es_empresarial
        )
    background_tasks.add_task(ejecutar_commando, comando)
    return RespuestaAsincrona(mensaje="Registro de usuario en proceso")