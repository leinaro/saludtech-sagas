from pulsar.schema import *
from dataclasses import dataclass, field
from query_data.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)
from query_data.seedwork.infraestructura.utils import time_millis
import uuid
    
class QueryEntrenamiento(Record):
    url_raw_data = String()
    partner_id = String()
    user_id = String()
    url_s3 = String()
    es_valido = Boolean()
    

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
    partner_id: String()
    user_id: String()
    url_raw_data: String()