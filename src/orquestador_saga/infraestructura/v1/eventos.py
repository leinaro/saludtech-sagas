from pulsar.schema import *
from processed_data.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
from processed_data.seedwork.infraestructura.utils import time_millis
from processed_data.modulos.infraestructura.v1 import TipoDatos
import uuid


class EventoCargaFinalizada(EventoIntegracion):
    partner_id = String()
    user_id = String()
    url_raw_data = String()
    url_s3 = String()

class EventoCargaFallida(EventoIntegracion):
    partner_id = String()
    user_id = String()
    url_raw_data = String()
    

class EventoDatosGuardados(EventoIntegracion):
    partner_id = String()
    user_id = String()
    url_raw_data = String()
    url_s3 = String()
    path = String()

class EventoProcesamientoDatosFallido(EventoIntegracion):
    partner_id = String()
    user_id = String()
    url_raw_data = String()
    url_s3 = String()


class EventoDatoProcesado(EventoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="EventoDatoProcesado")
    datacontenttype = String()
    service_name = String(default="processed_data.saludtech")
    #procesamiento_datos_iniciado = ProcesamientoDatosIniciado
    dato_procesado_guardado = EventoDatosGuardados
    #procesamiento_datos_cancelado = ProcesamientoDatosCancelado

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class EventoValidacionFinalizada(EventoIntegracion):
    partner_id = String()
    user_id = String()
    url_raw_data = String()
    url_s3 = String()
    path = String()
    es_valido = Boolean()

class EventoValidacionFallido(EventoIntegracion):
    partner_id = String()
    user_id = String()
    url_raw_data = String()
    url_s3 = String()
    path = String()


class EventoQueryEntrenamiendoFinalizado(EventoIntegracion):
    partner_id = String()
    user_id = String()
    url_raw_data = String()
    url_s3 = String()
    path = String()
    es_valido = Boolean()
    entrenamiendo_completado = Boolean()


class EventoQueryEntrenamiendoFallido(EventoIntegracion):
    partner_id = String()
    user_id = String()
    url_raw_data = String()
    url_s3 = String()
    path = String()
    es_valido = Boolean()

