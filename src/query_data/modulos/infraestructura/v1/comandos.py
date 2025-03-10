from pulsar.schema import *
from dataclasses import dataclass, field
from processed_data.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)
from processed_data.seedwork.infraestructura.utils import time_millis
from processed_data.modulos.infraestructura.v1 import TipoDatos
import uuid


@dataclass
class ComandoIniciarQueryEntrenamiento(Record):
    partner_id: str
    user_id: str
    url_raw_data: str

@dataclass
class ComandoCancelarQueryEntrenamiento(Record):
    partner_id: str
    user_id: str
    url_raw_data: str