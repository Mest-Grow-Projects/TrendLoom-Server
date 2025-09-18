from typing import List
from beanie import Document, Link
from pydantic import BaseModel
from app.database.models.base_mixin import TimestampMixin
from .user import User
from .products import Product


class CartItem(BaseModel):
    product_id: Link[Product]
    quantity: int = 1

class Cart(TimestampMixin, Document):
    user_id: Link[User]
    items: List[CartItem] = []

    class Settings:
        name = 'cart'