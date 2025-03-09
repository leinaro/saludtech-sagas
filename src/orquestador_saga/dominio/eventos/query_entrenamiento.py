from __future__ import annotations
from dataclasses import dataclass, field
from saludtech.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

class EventoQueryEntrenamiendo(EventoDominio):
    ...


@dataclass
class EventoQueryEntrenamiendoFinalizado(EventoQueryEntrenamiendo):
    partner_id: str
    user_id: str
    url_raw_data: str
    url_s3: str
    #tipo_processed_data: TipoDatos
    path: str
    entrenamiendo_completado: bool

    

@dataclass
class EventoQueryEntrenamiendoFallido(EventoQueryEntrenamiendo):
    partner_id: str
    user_id: str
    url_raw_data: str
    url_s3: str
    #tipo_processed_data: TipoDatos
    path: str

