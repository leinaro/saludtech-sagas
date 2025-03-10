from pulsar.schema import *

class EventoIntegracion(Record):
    time = String()
    ingestion = String()
    specversion = String(default="v1")
    type = String()
    datacontenttype = String()
    service_name = String(default="ingest_data") 