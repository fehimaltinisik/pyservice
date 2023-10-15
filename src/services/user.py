from io import BytesIO
from typing import List

from src.httpclients import user_api_client
from src.models.httpclient.mockuser import CreateUserAPIResponse
from src.models.httpclient.mockuser import GetUserAPIResponse
from src.models.router import CreateUserRequest


async def create_user(create_user_request: CreateUserRequest) -> CreateUserAPIResponse:
    create_user_api_response: CreateUserAPIResponse = await user_api_client.create_user(create_user_request)

    return create_user_api_response


async def get_user_by_id(user_id: id) -> GetUserAPIResponse:
    return await user_api_client.get_user(user_id)


def find_users_profile_picture_by_email(email: str) -> List[BytesIO]:
    """"""
    pass


def find_users_resume_by_email(email: str) -> List[BytesIO]:
    """"""
    pass
