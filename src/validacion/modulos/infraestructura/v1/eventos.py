from pulsar.schema import *
from validacion.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
from validacion.seedwork.infraestructura.utils import time_millis
from validacion.modulos.infraestructura.v1 import TipoCliente
import uuid



# NOTE En este caso usamos composición de eventos, donde un evento Usuario es constituido 
# por los eventos hijo. Recuerde que al ser mensajes inmutables, no consideramos conceptos como
# la herencia en los registros de esquemas. Por lo que el patrón de composición de mensajes se vuelve una buena opción
# esto nos permite seguir teniendo esquemas estrictos sin la necesidad de múltiples tópicos
class UsuarioRegistrado(Record):
    id = String()
    nombres = String()
    apellidos = String()
    email = String()
    tipo_cliente = TipoCliente
    fecha_creacion = Long()

class UsuarioValidado(Record):
    id = String()
    fecha_validacion = Long()

class UsuarioDesactivado(Record):
    id = String()
    fecha_desactivacion = Long()

class DataValidada(Record):
    id = String()
    url = String()
    fecha_validado = Long()

class DataCancelada(Record):
    id = String()
    url = String()
    fecha_procesado = Long()

class EventoUsuario(EventoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="EventoUsuario")
    datacontenttype = String()
    service_name = String(default="cliente.saludtech")
    usuario_registrado = UsuarioRegistrado
    usuario_validado = UsuarioValidado
    usuario_desactivado = UsuarioDesactivado

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class EventoValidacionFinalizada(EventoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="EventoValidacionFinaslizada")
    datacontenttype = String()
    service_name = String(default="validacion.saludtech")
    data_validada = DataValidada

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class EventoValidacionCancelada(EventoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String(default="v1")
    type = String(default="EventoValidacionCancelada")
    datacontenttype = String()
    service_name = String(default="validacion.saludtech")
    data_validada = DataCancelada

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
