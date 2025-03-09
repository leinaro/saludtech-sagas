from pulsar.schema import *
from dataclasses import dataclass, field
from processed_data.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)
from processed_data.seedwork.infraestructura.utils import time_millis
from processed_data.modulos.infraestructura.v1 import TipoDatos
import uuid

class ProcesamientoDatosIniciado():
#    id = String()
    url_raw_data = String()
    partner_id = String()
    user_id = String()
    #tipo_processed_data = TipoDatos
    fecha_inicio = Long()

class ProcesamientoDatosFallido():
 #   id = String()
    url_raw_data = String()
    partner_id = String()
    user_id = String()
    #tipo_processed_data = TipoDatos
    fecha_inicio = Long()

class DatoProcesadoGuardado():
    id = String()
    fecha_guardado = Long()

class ProcesamientoDatosCancelado():
    id = String()
    fecha_cancelacion = Long()

"""@dataclass
class ReservaCreada(EventoReserva):
    id_reserva: uuid.UUID = None
    id_cliente: uuid.UUID = None
    estado: str = None
    fecha_creacion: datetime = None
    monto: float = None
    monto_vat: float = None
    
@dataclass
class CreacionReservaFallida(EventoReserva):
    id_reserva: uuid.UUID = None
    id_cliente: uuid.UUID = None
    estado: str = None
    fecha_creacion: datetime = None
    monto: float = None
    monto_vat: float = None
    """