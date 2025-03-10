from dataclasses import dataclass, field
import uuid
import datetime

@dataclass
class Entidad:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    fecha_creacion: datetime.datetime = field(default_factory=datetime.datetime.now)
    fecha_actualizacion: datetime.datetime = field(default_factory=datetime.datetime.now)

@dataclass
class AgregacionRaiz(Entidad):
    id_correlacion: uuid.UUID = field(default_factory=uuid.uuid4) 