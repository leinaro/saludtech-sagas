"""Entidades del dominio de processed_data

En este archivo usted encontrará las entidades del dominio de processed_data

"""

from datetime import datetime
from processed_data.seedwork.dominio.entidades import Entidad, AgregacionRaiz
from dataclasses import dataclass, field

from .objetos_valor import Nombre, Email, Cedula, Rut


@dataclass
class DatoProcesado(Entidad):
    partner_id: str = None
    user_id: str = None
    url_raw_data: str = None
    #tipo_processed_data: str = None
