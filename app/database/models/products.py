from typing import List, Annotated
from enum import Enum
from beanie import Document, Indexed, Link
from pydantic import Field, BaseModel
import pymongo
from app.database.models.base_mixin import TimestampMixin
from app.database.models.user import User
from .category import Category
from .brands import Brand


class StockStatus(str, Enum):
    IN_STOCK = "in_stock"
    OUT_OF_STOCK = "out_of_stock"
    PRE_ORDER = "pre_order"

class Attributes(BaseModel):
    color: List[str]
    size: List[str]

class Product(Document, TimestampMixin):
    name: str
    description: str
    price: Annotated[float, Indexed()]
    currency: str = Field(default="USD")
    image: str
    detailsImage: List[str] | None = None
    brand: Link[Brand] | None = None
    category: Link[Category] | None = None
    attributes: List[Attributes] | None = None
    features: List[str] | None = None
    specifications: List[str] | None = None
    tags: List[str] | None = None
    stock: int = Field(ge=0, default=0)
    stockStatus: StockStatus | None = StockStatus.IN_STOCK
    is_featured: bool | None = None
    is_new: bool | None = None
    rating: float | None = None
    createdBy: Link[User]

    class Settings:
        name = "products"
        indexes = [
            [("createdBy", pymongo.ASCENDING)],
            [("brand", pymongo.ASCENDING)],
            [("tags", pymongo.ASCENDING)],
            [("category", pymongo.ASCENDING)],
            [("stockStatus", pymongo.ASCENDING)],
            [("is_featured", pymongo.ASCENDING)],
            [("is_new", pymongo.ASCENDING)],
        ]