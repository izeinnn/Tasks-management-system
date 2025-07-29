from pydantic import BaseModel, EmailStr
from pydantic import Field, field_validator
from typing import Optional


class UserBase(BaseModel):
    username: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Username must be 3-50 characters long.",
    )
    email: EmailStr

    @field_validator("username")
    def username_must_not_be_blank(cls, v):
        if not v.strip():
            raise ValueError("Username must not be blank.")
        return v


class UserCreate(UserBase):
    password: str = Field(
        ...,
        min_length=6,
        max_length=100,
        description="Password must be 6-100 characters long.",
    )


class UserOut(UserBase):
    pass

    class Config:
        from_attributes = True


class UserRead(UserBase):
    id: int

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    username: Optional[str] = Field(
        None,
        min_length=3,
        max_length=50,
        description="Username must be 3-50 characters long.",
    )
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(
        None,
        min_length=6,
        max_length=100,
        description="Password must be 6-100 characters long.",
    )
