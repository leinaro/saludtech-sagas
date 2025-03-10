"""Objetos valor del dominio de ingestación de datos

En este archivo usted encontrará los objetos valor del dominio de ingestación de datos

"""

from ingest_data.seedwork.dominio.objetos_valor import ObjetoValor
from dataclasses import dataclass
from enum import Enum

class EstadoIngestacion(str, Enum):
    INICIADA = "INICIADA"
    EN_PROCESO = "EN_PROCESO"
    FINALIZADA = "FINALIZADA"
    CANCELADA = "CANCELADA"

@dataclass(frozen=True)
class FuenteDato(ObjetoValor):
    nombre: str
    tipo: str
    configuracion: dict = None 