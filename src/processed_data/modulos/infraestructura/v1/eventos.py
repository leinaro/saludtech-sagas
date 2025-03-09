from pulsar.schema import *
from processed_data.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
from processed_data.seedwork.infraestructura.utils import time_millis
from processed_data.modulos.infraestructura.v1 import TipoDatos
import uuid



# NOTE En este caso usamos composición de eventos, donde un evento DatoProcesado es constituido 
# por los eventos hijo. Recuerde que al ser mensajes inmutables, no consideramos conceptos como
# la herencia en los registros de esquemas. Por lo que el patrón de composición de mensajes se vuelve una buena opción
# esto nos permite seguir teniendo esquemas estrictos sin la necesidad de múltiples tópicos
class ProcesamientoDatosIniciado(Record):
    id = String()
    url_raw_data = String()
    partner_id = String()
    user_id = String()
    #tipo_processed_data = TipoDatos
    fecha_inicio = Long()

class DatoProcesadoGuardado(Record):
    id = String()
    fecha_guardado = Long()
    path = String()

class ProcesamientoDatosCancelado(Record):
    id = String()
    fecha_cancelacion = Long()

class EventoDatoProcesado(EventoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="EventoDatoProcesado")
    datacontenttype = String()
    service_name = String(default="processed_data.saludtech")
    procesamiento_datos_iniciado = ProcesamientoDatosIniciado
    dato_procesado_guardado = DatoProcesadoGuardado
    procesamiento_datos_cancelado = ProcesamientoDatosCancelado

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)