from functools import singledispatch
from abc import ABC, abstractmethod

from orquestador_saga.aplicacion.comandos.validacion import ComandoIniciarValidacion
from processed_data.modulos.infraestructura.despachadores import Despachador

class Comando:
    ...

class ComandoHandler(ABC):
    @abstractmethod
    def handle(self, comando: Comando):
        raise NotImplementedError()

@singledispatch
def ejecutar_commando(comando):
    print("----------------")
    print(str(comando))
    if comando is not None:
        despachador = Despachador()
        despachador.publicar_mensaje(comando, "comando-iniciar-validacion")
    else:
        raise NotImplementedError(f'No existe implementación para el comando de tipo {type(comando).__name__}')