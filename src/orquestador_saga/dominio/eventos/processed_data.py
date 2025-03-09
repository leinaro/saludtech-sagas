from __future__ import annotations
from dataclasses import dataclass, field
from saludtech.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

class EventoDatoProcesado(EventoDominio):
    ...



@dataclass
class EventoProcesamientoDatos(EventoDatoProcesado):
#    id = String()
    url_raw_data = String()
    partner_id = String()
    user_id = String()
    #tipo_processed_data = TipoDatos

@dataclass
class EventoDatosGuardados(EventoDatoProcesado):
#    id = String()
    url_raw_data = String()
    partner_id = String()
    user_id = String()
    #tipo_processed_data = TipoDatos
    path = String()

@dataclass
class EventoProcesamientoDatosFallido(EventoDatoProcesado):
#    id = String()
    url_raw_data = String()
    partner_id = String()
    user_id = String()

    #tipo_processed_data = TipoDatos

    


