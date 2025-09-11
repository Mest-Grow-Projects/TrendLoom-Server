from datetime import datetime
from pydantic import BaseModel, Field
from app.core.config.constants import validations, patterns_regex
from typing import List
from app.database.models.products import Attributes, StockStatus
from beanie import PydanticObjectId


class ProductsSchema(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=50,
        pattern=patterns_regex["name"],
        description=validations["name"],
    )
    description: str = Field(min_length=2)
    price: float

    model_config = {"extra": "forbid"}


class UpdateProductSchema(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    images: List[str] | None = None
    attributes: List[Attributes] | None = None
    features: List[str] | None = None
    specifications: List[str] | None = None
    stockStatus: StockStatus | None = None
    is_featured: bool | None = None
    is_new: bool | None = None
    rating: float | None = None

    model_config = {"extra": "forbid"}


class ProductOut(BaseModel):
    id: PydanticObjectId
    name: str
    description: str
    price: float
    currency: str = Field(default="USD")
    images: List[str] | None = None
    attributes: List[Attributes] | None = None
    features: List[str] | None = None
    specifications: List[str] | None = None
    stockStatus: StockStatus
    is_featured: bool | None = None
    is_new: bool | None = None
    rating: float | None = None
    createdAt: datetime
    updatedAt: datetime


class ProductResponse(BaseModel):
    message: str
    data: ProductOut


class ProductsResponse(BaseModel):
    message: str
    data: List[ProductOut]

class MessageResponse(BaseModel):
    message: str