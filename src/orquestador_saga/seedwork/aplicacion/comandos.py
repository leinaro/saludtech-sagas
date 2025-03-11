from functools import singledispatch
from abc import ABC, abstractmethod

from processed_data.modulos.infraestructura.despachadores import Despachador

class Comando:
    ...

class ComandoHandler(ABC):
    @abstractmethod
    def handle(self, comando: Comando):
        raise NotImplementedError()

@singledispatch
def ejecutar_commando(comando):
    print(">>>>>>>> EJECUTA COMANDO "+str(comando))
    if comando is not None:
        match comando.datacontenttype:
            case "ComandoIniciarCargaDatos":
                despachador = Despachador()
                despachador.publicar_mensaje(comando, "comando-iniciar-carga-datos")
            case "ComandoCancelarCargaDatos":
                despachador = Despachador()
                despachador.publicar_mensaje(comando, "comando-cancelar-carga-datos")
            
            case "ComandoIniciarProcesamientoDatos":
                despachador = Despachador()
                despachador.publicar_mensaje(comando, "comando-iniciar-procesamiento-datos")
            case "ComandoCancelarProcesamientoDatos":
                despachador = Despachador()
                despachador.publicar_mensaje(comando, "comando-cancelar-procesamiento-datos")
            
            case "IniciarValidacion":
                despachador = Despachador()
                despachador.publicar_mensaje(comando, "comando-iniciar-validacion")
            case "ComandoCancelarValidacion":
                despachador = Despachador()
                despachador.publicar_mensaje(comando, "comando-cancelar-validacion")
            
            case "QueryEntrenamiento":
                despachador = Despachador()
                despachador.publicar_mensaje(comando, "comando-iniciar-query-entrenamiento")
            case "ComandoCancelarQueryEntrenamiento":
                despachador = Despachador()
                despachador.publicar_mensaje(comando, "comando-cancelar-query-entrenamiento")
    else:
        raise NotImplementedError(f'No existe implementación para el comando de tipo {type(comando).__name__}')