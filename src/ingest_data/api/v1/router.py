from fastapi import APIRouter
from .ingestacion.router import router as ingestacion_router


router = APIRouter()
router.include_router(ingestacion_router, prefix="/ingestacion", tags=["Ingestacion"]) 