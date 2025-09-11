from typing import List, Literal
from datetime import datetime
from beanie import PydanticObjectId
from pydantic import BaseModel, Field
from app.database.models.user import Gender, AccountStatus, Roles


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

class FilterQuery(BaseModel):
    name: str | None = None
    gender: Gender | None = None
    role: Roles | None = None
    account_status: AccountStatus | None = None
    order_by: Literal["created_at", "updated_at"] = "created_at"
    page: int = Field(1, ge=1)
    limit: int = Field(10, ge=1, le=50)

    model_config = {"extra": "forbid"}