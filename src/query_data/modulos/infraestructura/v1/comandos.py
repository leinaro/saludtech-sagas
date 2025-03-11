from pulsar.schema import *
from dataclasses import dataclass, field
from processed_data.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)
from processed_data.seedwork.infraestructura.utils import time_millis
from processed_data.modulos.infraestructura.v1 import TipoDatos
import uuid


class ComandoIniciarQueryEntrenamiento(ComandoIntegracion):
    partner_id: String()
    user_id: String()
    url_raw_data: String()

class ComandoCancelarQueryEntrenamiento(ComandoIntegracion):
    partner_id: String()
    user_id: String()
    url_raw_data: String()