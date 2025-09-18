from beanie import Document, Link, Indexed
from .user import User
from .base_mixin import TimestampMixin
from typing import Annotated
from pymongo import ASCENDING


class Category(Document, TimestampMixin):
    name: Annotated[str, Indexed()]
    description: str | None = None
    image: str | None = None
    parent_category: Link["Category"] | None = None
    createdBy: Link[User]

    class Settings:
        name = "categories"
        indexes = [
            [("name", ASCENDING)],
            [("createdBy", ASCENDING)],
            [("parent_category", ASCENDING)],
        ]