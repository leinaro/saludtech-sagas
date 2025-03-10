from pulsar.schema import *
from dataclasses import dataclass, field
from processed_data.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)
from processed_data.seedwork.infraestructura.utils import time_millis
from processed_data.modulos.infraestructura.v1 import TipoDatos
import uuid


class ProcesarDatos(Record):
    url_raw_data = String()
    partner_id = String()
    user_id = String()
    #tipo_processed_data = TipoDatos
    fecha_creacion = Long()

class GuardarDatoProcesado(Record):
    id = String()
    fecha_guardado = Long()

class CancelarProcesamientoDatos(Record):
    id = String()
    fecha_cacelacion = Long()

class ComandoIniciarProcesamientoDatos(ComandoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="ProcesarDatos")
    datacontenttype = String()
    service_name = String(default="processed_data.saludtech")
    data = ProcesarDatos

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ComandoGuardarDatoProcesado(ComandoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="GuardarDatoProcesado")
    datacontenttype = String()
    service_name = String(default="processed_data.saludtech")
    data = GuardarDatoProcesado

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ComandoCancelarProcesamientoDatos(ComandoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="CancelarProcesamientoDatos")
    datacontenttype = String()
    service_name = String(default="processed_data.saludtech")
    data = CancelarProcesamientoDatos

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class IniciarValidacion(Record):
    id = String()
    url = String()
    fecha_inicio_validacion = Long()


class CancelarValidacion(Record):
    id = String()
    url = String()
    fecha_cancelacion = Long()

class ComandoIniciarValidacion(ComandoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="IniciarValidacion")
    datacontenttype = String()
    service_name = String(default="validacion.saludtech")
    data = IniciarValidacion

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ComandoCancelarValidacion(ComandoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="CancelarValidacion")
    datacontenttype = String()
    service_name = String(default="validacion.saludtech")
    data = CancelarValidacion

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)