from typing import Generic, TypeVar
from pulsar.schema import *
from processed_data.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
from processed_data.seedwork.infraestructura.utils import time_millis
from processed_data.modulos.infraestructura.v1 import TipoDatos
import uuid



class CargaFinalizada(Record):
    traceId = String()
    partner_id = String()
    user_id = String()
    url_raw_data = String()
    url_s3 = String()

class CargaFallida(Record):
    traceId = String()
    partner_id = String()
    user_id = String()
    url_raw_data = String()

class ProcesamientoDatosFinalizado(Record):
    traceId = String()
    partner_id = String()
    user_id = String()
    url_raw_data = String()
    url_s3 = String()
    path = String()

class ProcesamientoDatosFallido(Record):
    traceId = String()
    partner_id = String()
    user_id = String()
    url_raw_data = String()
    url_s3 = String()

class ValidacionFinalizada(Record):
    traceId = String()
    partner_id = String()
    user_id = String()
    url_raw_data = String()
    url_s3 = String()
    path = String()
    es_valido = Boolean()

class ValidacionFallido(Record):
    traceId = String()
    partner_id = String()
    user_id = String()
    url_raw_data = String()
    url_s3 = String()
    path = String()
    
class QueryEntrenamiendoFinalizado(Record):
    traceId = String()
    partner_id = String()
    user_id = String()
    url_raw_data = String()
    url_s3 = String()
    path = String()
    es_valido = Boolean()
    entrenamiendo_completado = Boolean()

class QueryEntrenamiendoFallido(Record):
    traceId = String()
    partner_id = String()
    user_id = String()
    url_raw_data = String()
    url_s3 = String()
    path = String()
    es_valido = Boolean()



class EventoCargaFinalizada(EventoIntegracion):
    id = String()
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String(default=CargaFinalizada.__name__)
    service_name = String()
    data = CargaFinalizada
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class EventoCargaFallida(EventoIntegracion):
    id = String()
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String(default=CargaFallida.__name__)
    service_name = String()
    data = CargaFallida
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class EventoProcesamientoDatosFinalizado(EventoIntegracion):
    id = String()
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String(default=ProcesamientoDatosFinalizado.__name__)
    service_name = String()
    data = ProcesamientoDatosFinalizado
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class EventoProcesamientoDatosFallido(EventoIntegracion):
    id = String()
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String(default=ProcesamientoDatosFallido.__name__)
    service_name = String()
    data = ProcesamientoDatosFallido
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class EventoValidacionFinalizada(EventoIntegracion):
    id = String()
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String(default=ValidacionFinalizada.__name__)
    service_name = String()
    data = ValidacionFinalizada
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class EventoValidacionFallido(EventoIntegracion):
    id = String()
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String(default=ValidacionFallido.__name__)
    service_name = String()
    data = ValidacionFallido
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
class EventoQueryEntrenamiendoFinalizado(EventoIntegracion):
    id = String()
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String(default=QueryEntrenamiendoFinalizado.__name__)
    service_name = String()
    data = QueryEntrenamiendoFinalizado
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class EventoQueryEntrenamiendoFallido(EventoIntegracion):
    id = String()
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String(default=QueryEntrenamiendoFallido.__name__)
    service_name = String()
    data = QueryEntrenamiendoFallido
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
