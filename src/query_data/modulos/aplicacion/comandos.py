from query_data.seedwork.aplicacion.comandos import Comando, ComandoHandler
from query_data.seedwork.aplicacion.comandos import ejecutar_commando as comando
from query_data.modulos.dominio.entidades import IngestedData
from dataclasses import dataclass
import datetime
import time

@dataclass
class ComandoIniciarQueryEntrenamiento(Comando):
    partner_id: str
    user_id: str
    url_raw_data: str

@dataclass
class ComandoCancelarQueryEntrenamiento(Comando):
    partner_id: str
    user_id: str
    url_raw_data: str


class IniciarEntrenamientoHandler(ComandoHandler):
    
    def handle(self, comando: ComandoIniciarQueryEntrenamiento):
        data_ingest = IngestedData(
            data=comando.url_raw_data,
            partner_id = comando.partner_id,
        )
        return data_ingest


class CancelarEntrenamientoHandler(ComandoHandler):
    
    def handle(self, comando: ComandoCancelarQueryEntrenamiento):
        data_ingest = IngestedData(
            data=comando.url_raw_data,
            partner_id = comando.partner_id,
        )
        return data_ingest


@comando.register(ComandoIniciarQueryEntrenamiento)
def ejecutar_comando_iniciar_entrenamiento(comando: ComandoIniciarQueryEntrenamiento):
    handler = IniciarEntrenamientoHandler()
    handler.handle(comando)


@comando.register(ComandoCancelarQueryEntrenamiento)
def ejecutar_comando_cancelar_entrenamiento(comando: ComandoCancelarQueryEntrenamiento):
    handler = CancelarEntrenamientoHandler()
    handler.handle(comando)