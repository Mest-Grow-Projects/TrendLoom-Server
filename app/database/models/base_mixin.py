from datetime import datetime
from pydantic import Field

class TimestampMixin:
    createdAt: datetime = Field(default_factory=datetime.now)
    updatedAt: datetime = Field(default_factory=datetime.now)