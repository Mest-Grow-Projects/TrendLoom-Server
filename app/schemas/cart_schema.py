from pydantic import BaseModel
from typing import List
from beanie import PydanticObjectId

class AddToCartRequest(BaseModel):
    product_id: PydanticObjectId
    quantity: int = 1

class UpdateCartItemRequest(BaseModel):
    product_id: PydanticObjectId
    quantity: int

class CartItemResponse(BaseModel):
    product_id: PydanticObjectId
    quantity: int

class CartResponse(BaseModel):
    user_id: PydanticObjectId
    items: List[CartItemResponse]