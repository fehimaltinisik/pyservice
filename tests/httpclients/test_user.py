from typing import Dict
from unittest.mock import Mock

import pytest
from pytest_mock import MockerFixture as Mocker

from src.exceptions.user import OperationError
from src.httpclients import user_api_client
from src.models.httpclient import CreateUserAPIResponse
from src.models.httpclient import GetUserAPIResponse
from tests.utils.models import HTTPClientModelTestUtils
from tests.utils.models import RouterModelTestUtils


class TestCreateUserAPIRequest:
    @pytest.fixture(scope='function')
    def mocked_http_client(self, mocker: Mocker):
        return mocker.patch('src.httpclients.user_api_client.HTTPClient', new=mocker.AsyncMock())

    @pytest.mark.asyncio
    async def test_should_return_correctly_when_called(self, mocked_http_client: Mock):
        http_client_response: Dict = HTTPClientModelTestUtils.create_user_api_response_payload
        mocked_http_client.request.return_value = http_client_response

        create_user_api_response: CreateUserAPIResponse = await user_api_client.create_user(
            RouterModelTestUtils.create_user_request)

        mocked_http_client.request.assert_called()
        assert create_user_api_response.dict() == http_client_response

    @pytest.mark.asyncio
    async def test_should_raise_operational_error_when_httpclient_returns_empty_response(
            self, mocked_http_client: Mock):
        mocked_http_client.request.return_value = {}

        with pytest.raises(OperationError):
            await user_api_client.create_user(RouterModelTestUtils.create_user_request)
        mocked_http_client.request.assert_called()


class TestUserAPIRequest:
    @pytest.fixture(scope='function')
    def mocked_http_client(self, mocker: Mocker):
        return mocker.patch('src.httpclients.user_api_client.HTTPClient', new=mocker.AsyncMock())

    @pytest.mark.asyncio
    async def test_should_return_correctly_when_called(self, mocked_http_client: Mock):
        http_client_response: Dict = HTTPClientModelTestUtils.get_user_api_response_payload
        mocked_http_client.request.return_value = http_client_response

        get_user_api_response: GetUserAPIResponse = await user_api_client.get_user(1)

        mocked_http_client.request.assert_called()
        assert get_user_api_response.dict() == http_client_response
