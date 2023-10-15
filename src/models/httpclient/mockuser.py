from typing import Optional

from src.config.dto import DataTransferObject


class Address(DataTransferObject):
    class Geo(DataTransferObject):
        lat: str
        lng: str

    street: str
    suite: str
    city: str
    zipcode: str
    geo: Geo


class Company(DataTransferObject):
    name: str
    catchPhrase: str
    bs: str


class GetUserAPIResponse(DataTransferObject):
    id: int
    name: str
    username: str
    email: str
    address: Optional[Address]
    phone: Optional[str]
    website: Optional[str]
    company: Optional[Company]


class CreateUserAPIRequest(DataTransferObject):
    name: str
    username: str
    email: str


class CreateUserAPIResponse(DataTransferObject):
    id: int
    name: str
    username: str
    email: str
    address: Optional[Address]
    phone: Optional[str]
    website: Optional[str]
    company: Optional[Company]
