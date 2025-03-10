""" Fábricas para la creación de objetos del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de vuelos

"""

from .entidades import Reserva
from .reglas import MinimoUnItinerario, RutaValida
from .excepciones import TipoObjetoNoExisteEnDominioVuelosExcepcion
from orquestador_saga.seedwork.dominio.repositorios import Mapeador, Repositorio
from orquestador_saga.seedwork.dominio.fabricas import Fabrica
from orquestador_saga.seedwork.dominio.entidades import Entidad
from orquestador_saga.seedwork.dominio.eventos import EventoDominio
from dataclasses import dataclass

@dataclass
class _FabricaSagas(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad) or isinstance(obj, EventoDominio):
            return mapeador.entidad_a_dto(obj)
        else:
            reserva: Reserva = mapeador.dto_a_entidad(obj)

            self.validar_regla(MinimoUnItinerario(reserva.itinerarios))
            [self.validar_regla(RutaValida(ruta)) for itin in reserva.itinerarios for odo in itin.odos for segmento in odo.segmentos for ruta in segmento.legs]
            
            return reserva

@dataclass
class FabricaSagas(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Reserva.__class__:
            fabrica_saga = _FabricaSagas()
            return fabrica_saga.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioVuelosExcepcion()