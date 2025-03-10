from ingest_data.modulos.infraestructura.despachadores import Despachador
from ingest_data.modulos.infraestructura.v1.eventos import DatoIngestado, EventoIngestacionFinalizada
from ingest_data.seedwork.aplicacion.comandos import Comando, ComandoHandler
from ingest_data.seedwork.aplicacion.comandos import ejecutar_commando as comando
from ingest_data.modulos.dominio.entidades import Dato, Ingestacion
from dataclasses import dataclass
import datetime
import time

from ingest_data.seedwork.infraestructura import utils

@dataclass
class ComandoIniciarIngestacion(Comando):
    id : str
    fuente : str
    fecha_inicio_ingestacion : str

class IniciarIngestacionHandler(ComandoHandler):

    def a_entidad(self, comando: ComandoIniciarIngestacion) -> Ingestacion:
        params = dict(
            id=comando.id,
            fuente=comando.fuente,
            fecha_inicio=datetime.datetime.now()
        )

        ingestacion = Ingestacion(**params)
        return ingestacion
        

    def handle(self, comando: ComandoIniciarIngestacion):
        ingestacion = self.a_entidad(comando)
        # Aquí se implementaría la lógica para iniciar la ingestación
        # Por ejemplo, guardar en la base de datos, publicar eventos, etc.
        print(f"Iniciando ingestación con ID: {ingestacion.id} desde la fuente: {ingestacion.fuente}")
        

@comando.register(ComandoIniciarIngestacion)
def ejecutar_comando_iniciar_ingestacion(comando: ComandoIniciarIngestacion):
    handler = IniciarIngestacionHandler()
    handler.handle(comando) 