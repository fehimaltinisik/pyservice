from pydantic import BaseModel
from pydantic.utils import to_camel


class DataTransferObjectConfig:
    alias_generator = to_camel
    allow_population_by_field_name = True


class DataTransferObject(BaseModel):
    class Config(DataTransferObjectConfig):
        pass
