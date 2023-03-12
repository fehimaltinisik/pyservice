from fastapi import Query

from src.examples.user import EMAIL
from src.examples.user import FIRST_NAME
from src.examples.user import LAST_NAME
from src.models import Name


def inject_name(
        name: str = Query(..., title="Name", min_length=2, example=FIRST_NAME),
        surname: str = Query(..., title="Surname", min_length=2, example=LAST_NAME)) -> Name:
    """"""
    return Name(name, surname)


def inject_email(email: str = Query(..., title="Email", example=EMAIL)) -> str:
    """"""
    return email
