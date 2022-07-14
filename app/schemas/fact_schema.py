from typing import Union

from .base_schema import BaseSchema


class FactBase(BaseSchema):
    title: str
    description: str
    source: Union[str, None] = None
    user_id: int
    pet_id: int


class FactCreate(FactBase):
    pass


class FactOut(FactBase):
    id: int
