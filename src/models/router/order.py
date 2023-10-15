from datetime import datetime

from pydantic import Field

from src.config.dto import DataTransferObject


class CreateOrderRequest(DataTransferObject):
    customer_id: int = Field(..., min=0, max=2_147_483_647)


class CreateOrderResponse(DataTransferObject):
    id: int
    customer_id: str
    total: str
    created_at: datetime
    updated_at: datetime


class GetOrderByIdResponse(DataTransferObject):
    id: int
    customer_id: str
    total: str
    created_at: datetime
    updated_at: datetime
