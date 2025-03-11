from __future__ import annotations
from dataclasses import dataclass, field
from orquestador_saga.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

class EventoCarga(EventoDominio):
    ...


@dataclass
class EventoCargaFinalizada(EventoCarga):
    traceId: str = ""
    partner_id: str = ""
    user_id: str = ""
    url_raw_data: str = ""
    url_s3: str = ""

@dataclass
class EventoCargaFallida(EventoCarga):
    traceId: str = ""
    partner_id: str = ""
    user_id: str = ""
    url_raw_data: str = ""
