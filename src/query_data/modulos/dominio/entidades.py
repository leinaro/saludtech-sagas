"""Entidades del dominio de cliente

En este archivo usted encontrará las entidades del dominio de cliente

"""

from datetime import datetime
from cliente.seedwork.dominio.entidades import Entidad, AgregacionRaiz
from dataclasses import dataclass, field

from .objetos_valor import Nombre, Email, Cedula, Rut

@dataclass
class IngestedData(Entidad):
    nombre: str = field(default="")
    partner_id: int = field(default=0)