from pydantic import BaseSettings
from typing import Any

class Config(BaseSettings):
    APP_VERSION: str = "1.0.0"
    TITLE: str = "Ingest Data SaludTech"
    DESCRIPTION: str = "Microservicio para la ingestación de datos"
