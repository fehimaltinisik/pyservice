from typing import Dict

from src.definitions.api import API
from src.exceptions import UserNotFound
from src.exceptions.user import OperationError
from src.clients.httpclient import HTTPClient
from src.mappers import user_mapper
from src.models.httpclient import CreateUserAPIRequest
from src.models.httpclient import CreateUserAPIResponse
from src.models.httpclient import GetUserAPIResponse
from src.models.router import CreateUserRequest


async def create_user(create_user_request: CreateUserRequest) -> CreateUserAPIResponse:
    create_user_api_request: CreateUserAPIRequest = user_mapper.map_create_user_request_to_create_user_api_request(
        create_user_request)
    response: Dict = await HTTPClient.request(
        API.MOCK_USER,
        'POST',
        '/users',
        body=create_user_api_request.dict())
    if not response:
        raise OperationError(f"Failed to create user:{create_user_request.email}")

    return CreateUserAPIResponse(**response)


async def get_user(user_id: int) -> GetUserAPIResponse:
    response: Dict = await HTTPClient.request(API.MOCK_USER, 'GET', f'/users/{user_id}')
    if not response:
        raise UserNotFound(f"user:{user_id} not found!")

    return GetUserAPIResponse(**response)
