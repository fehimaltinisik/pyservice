from datetime import datetime
from random import randint
from typing import Dict

from src.models.httpclient import CreateUserAPIRequest
from src.models.httpclient import CreateUserAPIResponse
from src.models.httpclient import GetUserAPIResponse
from src.models.router import CreateUserRequest
from src.models.router import CreateUserResponse
from src.models.router import GetUserByIdResponse


def map_create_user_request_to_create_user_api_request(create_user_request: CreateUserRequest) -> CreateUserAPIRequest:
    """Convert CreateUserRequest to CreateUserAPIRequest."""
    return CreateUserAPIRequest(
        name=f"{create_user_request.first} {create_user_request.last}".title(),
        username=create_user_request.email,
        email=create_user_request.email)


def map_create_user_api_response_to_create_user_response(
        create_user_api_response: CreateUserAPIResponse) -> CreateUserResponse:
    """Convert CreateUserAPIResponse to CreateUserResponse."""
    return CreateUserResponse(
        **create_user_api_response.dict(include={'id', 'email'}),
        **_user_name_to_first_and_last_name(create_user_api_response.name),
        birthdate=_random_birthday())


def map_get_user_api_response_to_get_user_by_id_response(
        get_user_api_response: GetUserAPIResponse) -> GetUserByIdResponse:
    """Convert GetUserAPIResponse to GetUserByIdResponse."""

    return GetUserByIdResponse(
        **get_user_api_response.dict(include={'id', 'email'}),
        **_user_name_to_first_and_last_name(get_user_api_response.name),
        birthdate=_random_birthday())


def _user_name_to_first_and_last_name(user_name: str) -> Dict:
    """Convert username to first and last name."""
    name_parts = user_name.split(' ')
    first = ' '.join(name_parts[:-1])
    last = name_parts[-1]

    return {'first': first, 'last': last}


def _random_birthday() -> datetime:
    """Generate a random birthday."""
    return datetime(
        year=randint(1970, 2023),
        month=randint(1, 12),
        day=randint(1, 28))
