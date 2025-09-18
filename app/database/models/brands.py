from beanie import Document, Link, Indexed
from .user import User
from .base_mixin import TimestampMixin
from typing import Annotated
from pymongo import ASCENDING


class Brand(Document, TimestampMixin):
    name: Annotated[str, Indexed(unique=True)]
    logo: str
    description: str | None = None
    createdBy: Link[User]

    class Settings:
        name = "brands"
        indexes = [
            [("name", ASCENDING)],
            [("createdBy", ASCENDING)],
        ]