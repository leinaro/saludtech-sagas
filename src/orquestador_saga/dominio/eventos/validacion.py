from __future__ import annotations
from dataclasses import dataclass, field
from saludtech.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

class EventoValidacion(EventoDominio):
    ...

@dataclass
class EventoValidacionFinalizada(EventoValidacion):
#    id = String()
    url_raw_data = String()
    partner_id = String()
    user_id = String()
    #tipo_processed_data = TipoDatos
    path = String()
    es_valido: Bool()



@dataclass
class EventoValidacionFallido(EventoValidacion):
#    id = String()
    url_raw_data = String()
    partner_id = String()
    user_id = String()
    path = String()
    es_valido: Bool()
    #tipo_processed_data = TipoDatos