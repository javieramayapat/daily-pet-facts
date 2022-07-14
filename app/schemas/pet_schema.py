from .base_schema import BaseSchema


class PetBase(BaseSchema):
    name: str


class FactCreate(PetBase):
    pass


class FactOut(PetBase):
    id: int
