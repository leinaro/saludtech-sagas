from ingest_data.modulos.infraestructura.despachadores import Despachador
from ingest_data.modulos.infraestructura.v1.eventos import DatoIngestado, EventoDatoIngestado
from ingest_data.seedwork.aplicacion.comandos import Comando, ComandoHandler
from ingest_data.seedwork.aplicacion.comandos import ejecutar_commando as comando
from ingest_data.modulos.dominio.entidades import Dato
from dataclasses import dataclass
import datetime
import time
import json

from ingest_data.seedwork.infraestructura import utils

@dataclass
class ComandoIngestarDato(Comando):
    id : str
    fuente : str
    contenido : str
    fecha_ingestacion : str

class IngestarDatoHandler(ComandoHandler):

    def a_entidad(self, comando: ComandoIngestarDato) -> Dato:
        contenido = json.loads(comando.contenido) if isinstance(comando.contenido, str) else comando.contenido
        params = dict(
            id=comando.id,
            fuente=comando.fuente,
            contenido=contenido,
            fecha_ingestacion=datetime.datetime.now()
        )

        dato = Dato(**params)
        return dato
        

    def handle(self, comando: ComandoIngestarDato):
        dato = self.a_entidad(comando)
        # Aquí se implementaría la lógica para ingestar el dato
        # Por ejemplo, guardar en la base de datos, publicar eventos, etc.
        print(f"Dato ingestado con ID: {dato.id} desde la fuente: {dato.fuente}")
        
        # Publicar evento de dato ingestado
        payload = DatoIngestado(id = dato.id, fuente = dato.fuente, fecha_ingestacion = utils.time_millis())
        evento = EventoDatoIngestado(
            time=utils.time_millis(),
            ingestion=utils.time_millis(),
            datacontenttype=DatoIngestado.__name__,
            data = payload
        )
        despachador = Despachador()
        despachador.publicar_mensaje(evento, "evento-dato-ingestado")
        

@comando.register(ComandoIngestarDato)
def ejecutar_comando_ingestar_dato(comando: ComandoIngestarDato):
    handler = IngestarDatoHandler()
    handler.handle(comando) 