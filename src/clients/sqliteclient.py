import functools
import os
from enum import Enum
from typing import Optional

from loguru import logger
from sqlalchemy.future import Engine
from sqlmodel import SQLModel
from sqlmodel import Session
from sqlmodel import create_engine
from src.entities import *

CONNECTION = os.environ.get('SQLITE_CONNECTION', 'orders.db')


class SQLiteClient:
    class Table(str, Enum):
        ORDERS: str = 'orders'

    engine: Optional[Engine] = None

    @classmethod
    def init(cls):
        cls.engine = create_engine(f'sqlite:///{CONNECTION}', echo=True)
        SQLModel.metadata.create_all(cls.engine)
        logger.info("Executed DDLs!")

    @classmethod
    def close(cls):
        logger.info("Connection to SQLite database closed!")


def get_engine(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(SQLiteClient.engine, *args, **kwargs)

        return result

    return wrapper


def in_session(_func=None, *, commit: bool = False):
    def in_session_decorator(func):
        @functools.wraps(func)
        def in_session_wrapper(*args, **kwargs):
            with Session(SQLiteClient.engine) as session:
                result = func(session, *args, **kwargs)

                if commit:
                    session.commit()

                return result

        return in_session_wrapper

    if _func is None:
        return in_session_decorator
    else:
        return in_session_decorator(_func)
