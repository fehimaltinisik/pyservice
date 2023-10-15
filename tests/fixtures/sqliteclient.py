import pytest

from src.clients.sqliteclient import SQLiteClient


@pytest.fixture(scope='function')
def sqlite_db_client() -> SQLiteClient:
    SQLiteClient.init()

    yield SQLiteClient

    SQLiteClient.close()


@pytest.fixture(scope='function')
def engine(sqlite_db_client: SQLiteClient):
    return sqlite_db_client.engine
