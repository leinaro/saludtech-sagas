import os
from functools import lru_cache
from typing import Any

from pydantic import BaseSettings


class DBSettings(BaseSettings):
    DB_USERNAME: str = os.getenv("DB_USERNAME", "postgres")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "postgres")
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: str = os.getenv("DB_PORT", "5432")
    DB_NAME: str = os.getenv("DB_NAME", "ingest_data")
    DB_URI_ASYNC: str = f"postgresql+asyncpg://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


@lru_cache()
def get_db_settings() -> DBSettings:
    return DBSettings() 