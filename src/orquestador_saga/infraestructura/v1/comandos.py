from pulsar.schema import *
from dataclasses import dataclass, field
from processed_data.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)
from processed_data.seedwork.infraestructura.utils import time_millis
from processed_data.modulos.infraestructura.v1 import TipoDatos
import uuid

class ComandoIniciarCargaDatos(ComandoIntegracion):
    traceId = String()
    partner_id = String()
    user_id = String()
    url_raw_data = String()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ComandoCancelarCargaDatos(ComandoIntegracion):
    traceId = String()
    partner_id = String()
    user_id = String()
    url_raw_data = String()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    
class ComandoIniciarProcesamientoDatos(ComandoIntegracion):
    traceId = String()
    partner_id = String()
    user_id = String()
    url_raw_data = String()
    url_s3 = String()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
class ComandoCancelarProcesamientoDatos(ComandoIntegracion):
    traceId = String()
    partner_id = String()
    user_id = String()
    url_raw_data = String()
    url_s3 = String() 
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
    
    
class ComandoIniciarValidacion(ComandoIntegracion):
    traceId = String()
    partner_id = String()
    user_id = String()
    url_raw_data = String()
    url_s3 = String()
    path = String()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
class ComandoCancelarValidacion(ComandoIntegracion):
    traceId = String()
    partner_id = String()
    user_id = String()
    url_raw_data = String()
    url_s3 = String()
    path = String()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ComandoIniciarQueryEntrenamiento(ComandoIntegracion):
    traceId = String()
    partner_id = String()
    user_id = String()
    url_raw_data = String()
    url_s3 = String()
    path = String()
    es_valido = Boolean()  
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  
    
class ComandoCancelarQueryEntrenamiento(ComandoIntegracion):
    traceId = String()
    partner_id = String()
    user_id = String()
    url_raw_data = String()
    url_s3 = String()
    path = String()
    es_valido = Boolean() 
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
