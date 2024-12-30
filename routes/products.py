"""Products"""

from fastapi import APIRouter # type: ignore

router = APIRouter()

@router.get("/products/")
async def products_get():
    """GET products"""
    return "Listado"
