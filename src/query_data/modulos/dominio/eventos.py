
from pulsar.schema import *
from dataclasses import dataclass, field
from query_data.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)
from query_data.seedwork.infraestructura.utils import time_millis
import uuid

class EventoQueryEntrenamientoFinalizado(Record):
    url_raw_data = String()
    partner_id = String()
    user_id = String()
    fecha_inicio = Long()

class ProcesamientoDatosFallido(Record):
    url_raw_data = String()
    partner_id = String()
    user_id = String()
    fecha_inicio = Long()