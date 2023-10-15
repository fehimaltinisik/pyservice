from datetime import datetime

from pydantic import Field

from src.config.dto import DataTransferObject


class CreateUserRequest(DataTransferObject):
    first: str = Field(..., min_length=3, max_length=32)
    last: str = Field(..., min_length=3, max_length=32)
    email: str = Field(..., min_length=7, max_length=32)
    password: str = Field(..., min_length=8, max_length=32, description="Password must be between 8 and 32 characters.")
    birth_year: int = Field(default=1900, ge=1900, le=2100)
    birth_month: int = Field(default=1, ge=1, le=12)
    birth_day: int = Field(default=1, ge=1, le=31)


class CreateUserResponse(DataTransferObject):
    id: str
    first: str
    last: str
    email: str
    birthdate: datetime


class GetUserByIdResponse(DataTransferObject):
    id: str
    first: str
    last: str
    email: str
    birthdate: datetime
