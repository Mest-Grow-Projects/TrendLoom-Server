from typing import List
from datetime import datetime
from beanie import PydanticObjectId
from pydantic import BaseModel
from app.models.user import Roles, AccountStatus, Gender


class UserInfo(BaseModel):
    id: PydanticObjectId
    name: str
    email: str
    phone: str | None = None
    address: str | None = None
    role: Roles
    accountStatus: AccountStatus
    gender: Gender | None = None
    avatar: str | None = None
    dob: datetime | None = None
    createdAt: datetime
    updatedAt: datetime


class UserResponse(BaseModel):
    message: str
    data: UserInfo

class UsersResponse(BaseModel):
    message: str
    data: List[UserInfo]

class UpdateUserInfo(BaseModel):
    name: str | None = None
    email: str | None = None
    phone: str | None = None
    address: str | None = None
    gender: Gender | None = None
    dob: datetime | None = None

class ChangeRole(BaseModel):
    role: Roles