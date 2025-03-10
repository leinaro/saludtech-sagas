from __future__ import annotations
from dataclasses import dataclass, field
from orquestador_saga.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

class EventoDatoProcesado(EventoDominio):
    ...



@dataclass
class EventoProcesamientoDatos(EventoDatoProcesado):
#    id = String()
    url_raw_data: str  = ""
    partner_id: str = ""
    user_id: str = ""

@dataclass
class EventoDatosGuardados(EventoDatoProcesado):
    url_raw_data: str  = ""
    partner_id: str = ""
    user_id: str = ""
    path = str = ""

@dataclass
class EventoProcesamientoDatosFallido(EventoDatoProcesado):
#    id = String()
    url_raw_data: str  = ""
    partner_id : str  = ""
    user_id: str  = ""

    #tipo_processed_data = TipoDatos

    


