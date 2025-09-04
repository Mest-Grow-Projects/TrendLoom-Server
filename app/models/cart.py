from typing import List
from beanie import Document
from beanie import PydanticObjectId
from pydantic import BaseModel
from app.models.base_mixin import TimestampMixin


class CartItem(BaseModel):
    product_id: PydanticObjectId
    quantity: int = 1

class Cart(TimestampMixin, Document):
    user_id: PydanticObjectId
    items: List[CartItem] = []

    class Settings:
        name = 'cart'