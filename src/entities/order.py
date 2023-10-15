from datetime import datetime
from datetime import timedelta
from sqlalchemy import DateTime

from sqlmodel import Column
from sqlmodel import Field
from sqlmodel import SQLModel


class Order(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    customer_id: int = Field(default=None)
    total: float = Field(default=0.0)

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow,
                                 sa_column=Column(DateTime(), onupdate=datetime.utcnow))

    @property
    def is_return_eligible(self):
        return_eligibility_period = timedelta(days=14)
        since_checkout: timedelta = (datetime.utcnow() - self.created_at)

        return return_eligibility_period > since_checkout
