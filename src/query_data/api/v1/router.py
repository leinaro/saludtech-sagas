from fastapi import APIRouter
from .query.router import router as query_router

router = APIRouter()
router.include_router(query_router, prefix="/query", tags=["query"])