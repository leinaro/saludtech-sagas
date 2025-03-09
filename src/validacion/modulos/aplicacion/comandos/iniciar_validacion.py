from validacion.seedwork.aplicacion.comandos import Comando, ComandoHandler
from validacion.seedwork.aplicacion.comandos import ejecutar_commando as comando
from validacion.modulos.dominio.entidades import ClienteNatural, ClienteEmpresa, Usuario, Validacion
from validacion.modulos.dominio.objetos_valor import Cedula, Email, Nombre, Rut 
from dataclasses import dataclass
import datetime
import time

@dataclass
class ComandoIniciarValidacion(Comando):
    id : str
    url : str
    fecha_inicio_validacion : str
    tipo: str

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
        

@comando.register(ComandoIniciarValidacion)
def ejecutar_comando_crear_reserva(comando: ComandoIniciarValidacion):
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    handler = IniciarValidacionHandler()
    handler.handle(comando)