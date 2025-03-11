from pulsar.schema import *
from dataclasses import dataclass, field
from processed_data.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)
from processed_data.seedwork.infraestructura.utils import time_millis
from processed_data.modulos.infraestructura.v1 import TipoDatos
import uuid

class CargarDatos(Record):
    url_raw_data = String()
    partner_id = String()
    user_id = String()
    
class ProcesarDatos(Record):
    url_raw_data = String()
    partner_id = String()
    user_id = String()
    url_s3 = String()
    
class IniciarValidacion(Record):
    url_raw_data = String()
    partner_id = String()
    user_id = String()
    url_s3 = String()

class QueryEntrenamiento(Record):
    url_raw_data = String()
    partner_id = String()
    user_id = String()
    url_s3 = String()
    es_valido = Boolean()
    
    

class ComandoIniciarCargaDatos(ComandoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="CargarDatos")
    datacontenttype = String()
    service_name = String(default="CargarDatos.saludtech")
    data = CargarDatos

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ComandoCancelarCargaDatos(ComandoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="CargarDatos")
    datacontenttype = String()
    service_name = String(default="CargarDatos.saludtech")
    data = CargarDatos

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class ComandoIniciarProcesamientoDatos(ComandoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="ProcesarDatos")
    datacontenttype = String()
    service_name = String(default="ProcesarDatos.saludtech")
    data = ProcesarDatos

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ComandoCancelarProcesamientoDatos(ComandoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="ProcesarDatos")
    datacontenttype = String()
    service_name = String(default="ProcesarDatos.saludtech")
    data = ProcesarDatos

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

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
    type = String(default="IniciarValidacion")
    datacontenttype = String()
    service_name = String(default="validacion.saludtech")
    data = IniciarValidacion

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
class ComandoIniciarQueryEntrenamiento(ComandoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="QueryEntrenamiento")
    datacontenttype = String()
    service_name = String(default="QueryEntrenamiento.saludtech")
    data = QueryEntrenamiento

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ComandoCancelarQueryEntrenamiento(ComandoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="QueryEntrenamiento")
    datacontenttype = String()
    service_name = String(default="QueryEntrenamiento.saludtech")
    data = QueryEntrenamiento

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)