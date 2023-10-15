from typing import Dict

from src.models.httpclient import CreateUserAPIRequest
from src.models.httpclient import CreateUserAPIResponse
from src.models.httpclient import GetUserAPIResponse
from tests.utils.resources import load_json_resource


class HTTPClientModelTestUtils:
    """Test utilities for HTTPClient model."""

    RESOURCE_PATH: str = 'models.httpclient'

    create_user_api_request_payload: Dict = load_json_resource(RESOURCE_PATH, 'createuserapirequest.json')
    create_user_api_response_payload: Dict = load_json_resource(RESOURCE_PATH, 'createuserapiresponse.json')
    get_user_api_response_payload: Dict = load_json_resource(RESOURCE_PATH, 'getuserapiresponse.json')

    create_user_api_request: CreateUserAPIRequest = CreateUserAPIRequest(**create_user_api_request_payload)
    create_user_api_response: CreateUserAPIResponse = CreateUserAPIResponse(**create_user_api_response_payload)
    get_user_api_response: GetUserAPIResponse = GetUserAPIResponse(**get_user_api_response_payload)
