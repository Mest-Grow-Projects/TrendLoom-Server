from fastapi import APIRouter, status, HTTPException
from .cart_service import cart_service
from app.schemas.cart_schema import AddToCartRequest
from beanie import PydanticObjectId
from pydantic import ValidationError

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

@router.get(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
    summary="Get products from cart"
)
async def get_from_cart(user_id: str):
    try:
        object_id = PydanticObjectId(user_id)
        return await cart_service.get_from_cart(object_id)
    except ValidationError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"The provided user_id '{user_id}' is not a valid Object ID.",
        )

@router.delete(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
    summary="Delete a product from cart"
)
async def delete_from_cart(user_id: str, product_id: str):
    return await cart_service.remove_from_cart(user_id, product_id)