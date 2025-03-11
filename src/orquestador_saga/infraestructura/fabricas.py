""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de vuelos

"""

"""
from dataclasses import dataclass, field
from orquestador_saga.seedwork.dominio.fabricas import Fabrica
from orquestador_saga.seedwork.dominio.repositorios import Repositorio
#from orquestador_saga.seedwork.infraestructura.vistas import Vista
#from orquestador_saga.infraestructura.vistas import VistaReserva
#from orquestador_saga.dominio.entidades import Reserva
#from orquestador_saga.dominio.repositorios import RepositorioProveedores, RepositorioReservas, RepositorioEventosReservas
from .repositorios import RepositorioReservasSQLAlchemy, RepositorioProveedoresSQLAlchemy, RepositorioEventosReservaSQLAlchemy
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioReservas:
            return RepositorioReservasSQLAlchemy()
        elif obj == RepositorioProveedores:
            return RepositorioProveedoresSQLAlchemy()
        elif obj == RepositorioEventosReservas:
            return RepositorioEventosReservaSQLAlchemy()
        else:
            raise ExcepcionFabrica(f'No existe fábrica para el objeto {obj}')

@dataclass
class FabricaVista(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Vista:
        if obj == Reserva:
            return VistaReserva()
        else:
            raise ExcepcionFabrica(f'No existe fábrica para el objeto {obj}')
            """
