from processed_data.modulos.infraestructura.v1 import TipoDatos
from processed_data.seedwork.aplicacion.comandos import Comando, ComandoHandler
from processed_data.seedwork.aplicacion.comandos import ejecutar_commando as comando
from processed_data.modulos.dominio.entidades import DatoProcesado
from processed_data.modulos.dominio.objetos_valor import Cedula, Email, Nombre, Rut 
from dataclasses import dataclass
import datetime
import time

@dataclass
class ComandoIniciarProcesamientoDatos(Comando):
    partner_id: str
    user_id: str
    url_raw_data: str
    #tipo_processed_data: TipoDatos

class IniciarProcesamientoDatosHandler(ComandoHandler):

    def a_entidad(self, comando: ComandoIniciarProcesamientoDatos) -> DatoProcesado:
        params = dict(
            partner_id=comando.partner_id,
            user_id = comando.user_id,
            url_raw_data = comando.url_raw_data,
            #tipo_processed_data = comando.tipo_processed_data,
            fecha_creacion = datetime.datetime.now(),
            fecha_actualizacion = datetime.datetime.now()
        )

        processed_data = DatoProcesado(**params)

        print("---------------------")
        print(str(processed_data))
        print("---------------------")
        
        return processed_data
        

    def handle(self, comando: ComandoIniciarProcesamientoDatos):

        dato_procesado = self.a_entidad(comando)
        
        
        


@comando.register(ComandoIniciarProcesamientoDatos)
def ejecutar_comando_iniciar_procesamiento_datos(comando: ComandoIniciarProcesamientoDatos):
    handler = IniciarProcesamientoDatosHandler()
    handler.handle(comando)