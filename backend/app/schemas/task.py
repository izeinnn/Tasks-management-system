from pydantic import BaseModel
from enum import Enum


class PriorityEnum(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


from pydantic import Field, field_validator
from typing import Optional


class TaskBase(BaseModel):
    title: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Title must be 3-100 characters long.",
    )
    priority: PriorityEnum

    @field_validator("title")
    def title_must_not_be_blank(cls, v):
        if not v.strip():
            raise ValueError("Title must not be blank.")
        return v


class TaskCreate(TaskBase):
    user_id: Optional[int] = None


class TaskRead(TaskBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True


class TaskUpdate(BaseModel):
    title: str | None = None
    priority: PriorityEnum | None = None
