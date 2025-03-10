from __future__ import annotations
from dataclasses import dataclass, field
from orquestador_saga.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

class EventoIngestaData(EventoDominio):
    ...


@dataclass
class EventoCargaFinalizada(EventoIngestaData):
    partner_id = String()
    user_id = String()
    url_raw_data = String()
    url_s3 = String()

@dataclass
class EventoCargaFallida(EventoIngestaData):
    partner_id = String()
    user_id = String()
    url_raw_data = String()
    url_s3 = String()
