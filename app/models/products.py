from typing import List, Annotated
from enum import Enum
from beanie import Document, Indexed
from datetime import datetime
from pydantic import Field, BaseModel
import pymongo

class StockStatus(str, Enum):
    IN_STOCK = "in_stock"
    OUT_OF_STOCK = "out_of_stock"
    PRE_ORDER = "pre_order"

class Attributes(BaseModel):
    color: List[str]
    size: List[str]

class Product(Document):
    name: str | None = None
    description: str | None = None
    price: Annotated[float, Indexed()] | None = None
    currency: str = Field(default="USD")
    images: List[str] | None = None
    attributes: List[Attributes] | None = None
    features: List[str] | None = None
    specifications: List[str] | None = None
    stockStatus: StockStatus | None = StockStatus.IN_STOCK
    is_featured: bool | None = None
    is_new: bool | None = None
    rating: float | None = None
    createdAt: datetime = Field(default_factory=datetime.now)
    updatedAt: datetime = Field(default_factory=datetime.now)

    class Settings:
        name = "products"
        indexes = [
            [("stockStatus", pymongo.ASCENDING)],
            [("is_featured", pymongo.ASCENDING)],
            [("is_new", pymongo.ASCENDING)],
        ]