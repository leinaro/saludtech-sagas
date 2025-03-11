from __future__ import annotations
from dataclasses import dataclass, field
from orquestador_saga.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

class EventoQueryEntrenamiendo(EventoDominio):
    ...


@dataclass
class EventoQueryEntrenamiendoFinalizado(EventoQueryEntrenamiendo):
    traceId: str = ""
    partner_id: str = ""
    user_id: str = ""
    url_raw_data: str = ""
    url_s3: str = ""
    path: str = ""
    es_valido: bool = True
    entrenamiendo_completado: bool = True

    

@dataclass
class EventoQueryEntrenamiendoFallido(EventoQueryEntrenamiendo):
    traceId: str = ""
    partner_id: str = ""
    user_id: str = ""
    url_raw_data: str = ""
    url_s3: str = ""
    path: str = ""
    es_valido: bool = True
    
