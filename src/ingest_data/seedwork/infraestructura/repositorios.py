from abc import ABC, abstractmethod
from uuid import UUID
from ingest_data.seedwork.dominio.entidades import Entidad

class Repositorio(ABC):
    @abstractmethod
    async def obtener_por_id(self, id: UUID) -> Entidad:
        ...

    @abstractmethod
    async def obtener_todos(self) -> list[Entidad]:
        ...

    @abstractmethod
    async def agregar(self, entity: Entidad):
        ...

    @abstractmethod
    async def actualizar(self, entity: Entidad):
        ...

    @abstractmethod
    async def eliminar(self, entity_id: UUID):
        ... 