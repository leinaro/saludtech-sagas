from fastapi import APIRouter
from .orquestador.router import router as processing_router


router = APIRouter()
router.include_router(processing_router, prefix="/orquestador", tags=["Orquestador"])
