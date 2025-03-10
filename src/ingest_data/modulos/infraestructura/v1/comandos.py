from pulsar.schema import *
from dataclasses import dataclass, field
from ingest_data.seedwork.infraestructura.schema.v1.comandos import ComandoIntegracion

class IniciarIngestacion(Record):
    id = String()
    fuente = String()
    fecha_inicio_ingestacion = String()

class ComandoIniciarIngestacion(ComandoIntegracion):
    data = IniciarIngestacion()

class IngestarDato(Record):
    id = String()
    fuente = String()
    contenido = String()
    fecha_ingestacion = String()

class ComandoIngestarDato(ComandoIntegracion):
    data = IngestarDato()

class CancelarIngestacion(Record):
    id = String()
    fecha_cancelacion = String()

class ComandoCancelarIngestacion(ComandoIntegracion):
    data = CancelarIngestacion() 