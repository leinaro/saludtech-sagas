from __future__ import annotations
from dataclasses import dataclass, field
from orquestador_saga.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

class EventoValidacion(EventoDominio):
    ...

@dataclass
class EventoValidacionFinalizada(EventoValidacion):
#    id = String()
    url_raw_data: str  = ""
    partner_id : str  = ""
    user_id: str  = ""
    path: str  = ""
    es_valido: bool  = True


@dataclass
class EventoValidacionFallido(EventoValidacion):
#    id = String()
    url_raw_data: str  = ""
    partner_id : str  = ""
    user_id: str  = ""
    path: str  = ""
    es_valido: bool  = True
    #tipo_processed_data = TipoDatos