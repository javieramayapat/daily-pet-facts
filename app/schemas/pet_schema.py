from .base_schema import BaseSchema


class PetBase(BaseSchema):
    name: str


class PetCreate(PetBase):
    pass


class PetOut(PetBase):
    id: int
