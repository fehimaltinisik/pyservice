from fastapi import APIRouter
from fastapi import Body
from fastapi import Path

from src.docs.order import CREATE_ORDER_REQUEST
from src.entities import Order
from src.mappers import order_mapper
from src.models.router import CreateOrderRequest
from src.models.router import CreateOrderResponse
from src.models.router import GetOrderByIdResponse
from src.services import order_service

router = APIRouter(prefix='/orders', tags=['order'])


@router.post("/id")
async def create_order(
        create_order_request: CreateOrderRequest = Body(..., examples=CREATE_ORDER_REQUEST)) -> CreateOrderResponse:
    """Create a new order."""
    order: Order = await order_service.create_order(create_order_request)
    create_order_response: CreateOrderResponse = order_mapper.map_order_to_create_order_response(order)

    return create_order_response


@router.get("/id/{order_id}")
async def get_order_by_id(
        order_id: int = Path(..., title="Order ID", alias='order_id', min=1, example=1)) -> GetOrderByIdResponse:
    """Get order by id."""
    order: Order = await order_service.get_order_by_id(order_id)
    get_order_by_id_response: GetOrderByIdResponse = order_mapper.map_order_to_get_order_by_id_response(order)

    return get_order_by_id_response
