from ingest_data.seedwork.aplicacion.handlers import Handler
from ingest_data.modulos.dominio.eventos import DatoIngestado, IngestacionIniciada, IngestacionFinalizada, IngestacionCancelada

class HandlerDatoIngestadoDominio(Handler):
    def handle(self, evento):
        print(f"Dato ingestado con ID: {evento.id_dato}")

class HandlerIngestacionIniciadaDominio(Handler):
    def handle(self, evento):
        print(f"Ingestación iniciada con ID: {evento.id_ingestacion}")

class HandlerIngestacionFinalizadaDominio(Handler):
    def handle(self, evento):
        print(f"Ingestación finalizada con ID: {evento.id_ingestacion}")

class HandlerIngestacionCanceladaDominio(Handler):
    def handle(self, evento):
        print(f"Ingestación cancelada con ID: {evento.id_ingestacion}") 