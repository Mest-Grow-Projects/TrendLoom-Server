from datetime import datetime
from pydantic import BaseModel, Field
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
    id: str = Field(..., alias="_id")
    user_id: str
    items: List[CartItemResponse]
    createdAt: datetime
    updatedAt: datetime

    class Config:
        from_attributes = True
        populate_by_name = True