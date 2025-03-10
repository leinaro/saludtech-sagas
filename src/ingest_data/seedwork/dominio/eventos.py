from dataclasses import dataclass
from datetime import datetime
import uuid

@dataclass
class EventoDominio:
    id: uuid.UUID = uuid.uuid4()
    fecha_evento: datetime = datetime.now() 