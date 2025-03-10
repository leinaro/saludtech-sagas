"""Entidades del dominio de ingestación de datos

En este archivo usted encontrará las entidades del dominio de ingestación de datos

"""

from datetime import datetime
from ingest_data.seedwork.dominio.entidades import Entidad, AgregacionRaiz
from dataclasses import dataclass, field
from typing import Dict, Any

@dataclass
class Dato(Entidad):
    id: str = None
    fuente: str = None
    contenido: Dict[str, Any] = field(default_factory=dict)
    fecha_ingestacion: datetime = None

@dataclass
class Ingestacion(AgregacionRaiz):
    id: str = None
    fuente: str = None
    fecha_inicio: datetime = None
    fecha_fin: datetime = None
    estado: str = "INICIADA"
    datos: list[Dato] = field(default_factory=list) 