from src.entities import Order
from src.models.router import CreateOrderRequest
from src.models.router import CreateOrderResponse
from src.models.router.order import GetOrderByIdResponse


def map_create_order_request_to_new_order(create_order_request: CreateOrderRequest) -> Order:
    """Maps a CreateOrderRequest to a new Order entity."""
    return Order(customer_id=create_order_request.customer_id)


def map_order_to_create_order_response(order: Order) -> CreateOrderResponse:
    """Maps an Order entity to a CreateOrderResponse."""
    return CreateOrderResponse(**order.dict())


def map_order_to_get_order_by_id_response(order: Order) -> GetOrderByIdResponse:
    """Maps an Order entity to a GetOrderByIdResponse."""
    return GetOrderByIdResponse(**order.dict())
