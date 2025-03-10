from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional

router = APIRouter()

@router.get("/")
async def get_ingestacion():
    return {"message": "Servicio de ingestación de datos"} 