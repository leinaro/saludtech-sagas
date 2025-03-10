from dataclasses import dataclass
from abc import ABC

class ObjetoValor:
    pass

@dataclass(frozen=True)
class Ciudad(ObjetoValor):
    nombre: str 