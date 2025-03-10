from ingest_data.modulos.infraestructura.despachadores import Despachador
from ingest_data.modulos.infraestructura.v1.eventos import DatoIngestado, EventoIngestacionCancelada
from ingest_data.seedwork.aplicacion.comandos import Comando, ComandoHandler
from ingest_data.seedwork.aplicacion.comandos import ejecutar_commando as comando
from ingest_data.modulos.dominio.entidades import Ingestacion
from dataclasses import dataclass
import datetime
import time

from ingest_data.seedwork.infraestructura import utils

@dataclass
class ComandoCancelarIngestacion(Comando):
    id : str
    fecha_cancelacion : str

class CancelarIngestacionHandler(ComandoHandler):

    def handle(self, comando: ComandoCancelarIngestacion):
        # Aquí se implementaría la lógica para cancelar la ingestación
        # Por ejemplo, actualizar en la base de datos, publicar eventos, etc.
        print(f"Cancelando ingestación con ID: {comando.id}")
        
        # Publicar evento de ingestación cancelada
        payload = DatoIngestado(id = comando.id, fuente = "N/A", fecha_ingestacion = utils.time_millis())
        evento = EventoIngestacionCancelada(
            time=utils.time_millis(),
            ingestion=utils.time_millis(),
            datacontenttype=DatoIngestado.__name__,
            data = payload
        )
        despachador = Despachador()
        despachador.publicar_mensaje(evento, "evento-ingestacion-cancelada")
        

@comando.register(ComandoCancelarIngestacion)
def ejecutar_comando_cancelar_ingestacion(comando: ComandoCancelarIngestacion):
    handler = CancelarIngestacionHandler()
    handler.handle(comando) 