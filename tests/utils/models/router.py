from typing import Dict

from src.models.router import CreateUserRequest
from tests.utils.resources import load_json_resource


class RouterModelTestUtils:
    RESOURCE_PATH: str = 'models.router'

    create_user_request_payload: Dict = load_json_resource(RESOURCE_PATH, 'createuserrequest.json')
    create_user_request: CreateUserRequest = CreateUserRequest(**create_user_request_payload)
