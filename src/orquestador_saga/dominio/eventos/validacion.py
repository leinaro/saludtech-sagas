from __future__ import annotations
from dataclasses import dataclass, field
from orquestador_saga.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

class EventoValidacion(EventoDominio):
    ...

@dataclass
class EventoValidacionFinalizada(EventoValidacion):
    traceId: str = ""
    partner_id: str = ""
    user_id: str = ""
    url_raw_data: str = ""
    url_s3: str = ""
    path: str = ""
    es_valido: bool = True
    


@dataclass
class EventoValidacionFallido(EventoValidacion):
    traceId: str = ""
    partner_id: str = ""
    user_id: str = ""
    url_raw_data: str = ""
    url_s3: str = ""
    path: str = ""
    