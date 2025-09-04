from enum import Enum
from typing import Annotated
from pydantic import EmailStr
from datetime import datetime
from beanie import Document, Indexed
import pymongo
from app.models.base_mixin import TimestampMixin

class Roles(str, Enum):
    CUSTOMER = "CUSTOMER"
    PRODUCT_ADMIN = "PRODUCT_ADMIN"
    ADMIN = "ADMIN"

class AccountStatus(str, Enum):
    VERIFIED = "VERIFIED"
    PENDING = "PENDING"
    SUSPENDED = "SUSPENDED"

class Gender(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    NON_BINARY = "NON_BINARY"

class User(Document, TimestampMixin):
    name: str
    email: Annotated[EmailStr, Indexed(unique=True)]
    phone: str | None = None
    address: str | None = None
    password: str
    role: Roles = Roles.CUSTOMER
    accountStatus: AccountStatus = AccountStatus.PENDING
    gender: Gender | None = None
    avatar: str | None = None
    dob: datetime | None = None

    class Settings:
        name = 'users'
        indexes = [
            [("role", pymongo.ASCENDING)],
            [("accountStatus", pymongo.ASCENDING)],
            [("createdAt", pymongo.DESCENDING)],
        ]