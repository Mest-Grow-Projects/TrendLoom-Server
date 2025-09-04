from fastapi import APIRouter, status
from .cart_service import cart_service
from app.schemas.cart_schema import AddToCartRequest

router = APIRouter(
    prefix="/cart",
    tags=["Cart"]
)

@router.post(
    "/{user_id}/add",
    status_code=status.HTTP_200_OK,
    summary="Add a product to cart"
)
async def add_to_cart(user_id: str, data: AddToCartRequest):
    return await cart_service.add_to_cart(user_id, data)