from abc import ABC, abstractmethod
from ingest_data.modulos.dominio.entidades import Dato, Ingestacion
from uuid import UUID

class RepositorioDatos(ABC):
    @abstractmethod
    async def obtener_por_id(self, id: UUID) -> Dato:
        ...

    @abstractmethod
    async def obtener_todos(self) -> list[Dato]:
        ...

    @abstractmethod
    async def agregar(self, dato: Dato):
        ...

    @abstractmethod
    async def actualizar(self, dato: Dato):
        ...

    @abstractmethod
    async def eliminar(self, dato_id: UUID):
        ... 