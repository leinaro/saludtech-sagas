from __future__ import annotations
from dataclasses import dataclass, field
from orquestador_saga.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

class EventoProcesamientoDatosFinalizado(EventoDominio):
    ...



@dataclass
class EventoProcesamientoDatos(EventoProcesamientoDatosFinalizado):
#    id = String()
    url_raw_data: str  = ""
    partner_id: str = ""
    user_id: str = ""
    url_s3: str = ""

@dataclass
class EventoProcesamientoDatosFinalizado(EventoProcesamientoDatosFinalizado):
    url_raw_data: str  = ""
    partner_id: str = ""
    user_id: str = ""
    url_s3: str = ""
    path = str = ""
    
@dataclass
class EventoProcesamientoDatosFallido(EventoProcesamientoDatosFinalizado):
#    id = String()
    url_raw_data: str  = ""
    partner_id : str  = ""
    user_id: str  = ""



