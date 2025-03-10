from ingest_data.seedwork.dominio.eventos import EventoDominio
from dataclasses import dataclass
from datetime import datetime

@dataclass
class DatoIngestado(EventoDominio):
    id_dato: str = None
    fuente: str = None
    fecha_ingestacion: datetime = None

@dataclass
class IngestacionIniciada(EventoDominio):
    id_ingestacion: str = None
    fuente: str = None
    fecha_inicio: datetime = None

@dataclass
class IngestacionFinalizada(EventoDominio):
    id_ingestacion: str = None
    fecha_fin: datetime = None

@dataclass
class IngestacionCancelada(EventoDominio):
    id_ingestacion: str = None
    fecha_cancelacion: datetime = None 