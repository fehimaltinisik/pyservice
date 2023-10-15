from src.entities import Order
from src.mappers import order_mapper
from src.models.router import CreateOrderRequest
from src.repositories import order_repository


async def create_order(create_order_request: CreateOrderRequest) -> Order:
    order: Order = order_mapper.map_create_order_request_to_new_order(create_order_request)
    order_repository.save_and_refresh(order)

    return order


async def get_order_by_id(user_id: id) -> Order:
    return order_repository.find_by_id(user_id)
