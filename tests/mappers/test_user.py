from typing import Dict

from src.mappers import user_mapper
from src.models.httpclient import CreateUserAPIRequest
from src.models.httpclient import CreateUserAPIResponse
from src.models.httpclient import GetUserAPIResponse
from src.models.router import CreateUserRequest
from src.models.router import CreateUserResponse
from src.models.router import GetUserByIdResponse
from tests.utils.models import HTTPClientModelTestUtils
from tests.utils.models import RouterModelTestUtils


class TestMapUsernameToFirstAndLastName:
    """._user_name_to_first_and_last_name"""

    def test_should_return_first_and_last_name(self):
        """Should return first and last name"""
        user_name: str = 'John Doe'
        first_and_last_name: Dict = user_mapper._user_name_to_first_and_last_name(user_name)

        assert first_and_last_name == {'first': 'John', 'last': 'Doe'}

    def test_should_return_multiple_given_names_and_a_last_name(self):
        """Should return first and last name"""
        user_name: str = 'John F. Doe'
        first_and_last_name: Dict = user_mapper._user_name_to_first_and_last_name(user_name)

        assert first_and_last_name == {'first': 'John F.', 'last': 'Doe'}


class TestMapCreateUserRequestToCreateUserAPIRequest:
    """.map_create_user_request_to_create_user_api_request"""

    def test_should_map_create_user_request_to_create_user_api_request(self):
        """Should init a CreateUserAPIRequest instance"""
        create_user_request: CreateUserRequest = RouterModelTestUtils.create_user_request
        create_user_api_request: CreateUserAPIRequest = user_mapper.map_create_user_request_to_create_user_api_request(
            create_user_request)

        assert create_user_api_request


class TestMapCreateUserAPIResponseToCreateUserResponse:
    """.map_create_user_api_response_to_create_user_response"""

    def test_should_map_create_user_api_response_to_create_user_response(self):
        """Should init a CreateUserResponse instance"""
        create_user_api_response: CreateUserAPIResponse = HTTPClientModelTestUtils.create_user_api_response
        create_user_response: CreateUserResponse = user_mapper.map_create_user_api_response_to_create_user_response(
            create_user_api_response)

        assert create_user_response


class TestMapGetUserAPIResponseToGetUserByIdResponse:
    """.map_get_user_api_response_to_get_user_by_id_response"""

    def test_should_map_get_user_api_response_to_get_user_by_id_response(self):
        """Should init a GetUserByIdResponse instance"""
        get_user_api_response: GetUserAPIResponse = HTTPClientModelTestUtils.get_user_api_response
        get_user_by_id_response: GetUserByIdResponse = user_mapper.map_get_user_api_response_to_get_user_by_id_response(
            get_user_api_response)

        assert get_user_by_id_response
