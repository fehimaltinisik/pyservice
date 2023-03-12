from io import BytesIO
from typing import List

from src.examples import user as user_example
from src.models import Name
from src.models import User


def find_user_by_name(name: Name) -> User:
    """"""
    return User(name=name, email=user_example.EMAIL, birthdate=user_example.BIRTHDATE)


def find_user_by_email_and_calculate_age(email: str) -> int:
    """"""
    name: Name = Name(first=user_example.FIRST_NAME, last=user_example.FIRST_NAME)
    user: User = User(name=name, email=email, birthdate=user_example.BIRTHDATE)

    return user.age()


def find_users_profile_picture_by_email(email: str) -> List[BytesIO]:
    """"""
    pass


def find_users_resume_by_email(email: str) -> List[BytesIO]:
    """"""
    pass
