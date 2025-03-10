from validacion.modulos.infraestructura.despachadores import Despachador
from validacion.modulos.infraestructura.v1.eventos import DataValidada, EventoValidacionFinalizada
from validacion.seedwork.aplicacion.comandos import Comando, ComandoHandler
from validacion.seedwork.aplicacion.comandos import ejecutar_commando as comando
from validacion.modulos.dominio.entidades import ClienteNatural, ClienteEmpresa, Usuario, Validacion
from validacion.modulos.dominio.objetos_valor import Cedula, Email, Nombre, Rut 
from dataclasses import dataclass
import datetime
import time

from validacion.seedwork.infraestructura import utils

@dataclass
class ComandoIniciarValidacion(Comando):
    id : str
    url : str
    fecha_inicio_validacion : str

class IniciarValidacionHandler(ComandoHandler):

    def a_entidad(self, comando: ComandoIniciarValidacion) -> Validacion:
        params = dict(
            id=comando.id,
            url = comando.url,
            fecha_validacion = datetime.datetime.now()
        )

        validacion = Validacion(**params)
        return validacion
        

    def handle(self, comando: ComandoIniciarValidacion):
        validacion = self.a_entidad(comando)
        payload = DataValidada(id = validacion.id, url = validacion.url, fecha_validacion = utils.time_millis())
        evento = EventoValidacionFinalizada(
            time=utils.time_millis(),
            ingestion=utils.time_millis(),
            datacontenttype=DataValidada.__name__,
            data = payload
        )
        despachador = Despachador()
        despachador.publicar_mensaje(evento, "evento-validacion-finalizada")


        

@comando.register(ComandoIniciarValidacion)
def ejecutar_comando_iniciar_validacion(comando: ComandoIniciarValidacion):
    handler = IniciarValidacionHandler()
    handler.handle(comando)