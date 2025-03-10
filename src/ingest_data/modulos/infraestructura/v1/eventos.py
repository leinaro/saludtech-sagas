from pulsar.schema import *
from dataclasses import dataclass, field
from ingest_data.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion

class DatoIngestado(Record):
    id = String()
    fuente = String()
    fecha_ingestacion = String()

class EventoDatoIngestado(EventoIntegracion):
    data = DatoIngestado()

class EventoIngestacionFinalizada(EventoIntegracion):
    data = DatoIngestado()

class EventoIngestacionCancelada(EventoIntegracion):
    data = DatoIngestado() 