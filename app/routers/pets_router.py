from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlalchemy.orm import Session

from ..dependencies import get_db
from ..schemas import pet_schema
from ..services import pet_service

router = APIRouter(prefix="/pets",
                   tags=["Pets"],
                   dependencies=[Depends(get_db)])


@router.get(path="/", response_model=list[pet_schema.PetOut], status_code=status.HTTP_200_OK)
def get_pet_types(db: Session = Depends(get_db)):
    pets = pet_service.get_pets(db=db)
    return pets


@router.get(path="/{pet_id}", response_model=pet_schema.PetOut, status_code=status.HTTP_200_OK)
def get_pet(pet_id: int = Path(..., gt=0, example=1), db: Session = Depends(get_db)):
    pet = pet_service.get_pet(db=db, pet_id=pet_id)
    if pet is None:
        raise HTTPException(status_code=404, detail="Pet not found")
    return pet
