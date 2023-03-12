from datetime import date
from datetime import datetime
from typing import NamedTuple

from pydantic import BaseModel
from pydantic import Field


class Name(NamedTuple):
    first: str = ""
    last: str = ""

    def full(self) -> str:
        return (self.first + self.last).title()


class User(BaseModel):
    name: Name = Field(...)
    email: str = Field(...)
    birthdate: datetime = Field(default_factory=lambda: datetime(1900, 1, 1, 0, 0, 0, 0))

    def age(self) -> int:
        now: datetime = datetime.utcnow()
        today: date = now.date()

        return today.year - self.birthdate.year
