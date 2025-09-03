from app.models.products import Product
from fastapi import HTTPException, status
from app.core.constants import status_messages

async def check_existing_product(name: str) -> bool:
    existing_product = await Product.find_one(Product.name == name)
    if existing_product:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=status_messages["product_conflict"]
        )
    return False

async def find_product_by_id(product_id: str) -> Product:
    product = await Product.get(product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=status_messages["product_not_found"]
        )
    return product