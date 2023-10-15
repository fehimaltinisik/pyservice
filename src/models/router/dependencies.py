from fastapi import Path
from fastapi import Query

from src.examples.user import EMAIL
from src.examples.user import FIRST_NAME
from src.examples.user import LAST_NAME
from src.models import Name


def on_user_id(
        user_id: int = Path(..., title="User ID", alias='user_id', min=1, example=1)) -> int:
    """"""
    return user_id


def on_name(
        name: str = Query(..., title="Name", min_length=2, example=FIRST_NAME),
        surname: str = Query(..., title="Surname", min_length=2, example=LAST_NAME)) -> Name:
    """"""
    return Name(name, surname)


def on_email(email: str = Query(..., title="Email", example=EMAIL)) -> str:
    """"""
    return email
