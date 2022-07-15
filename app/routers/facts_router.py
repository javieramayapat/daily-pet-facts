from fastapi import APIRouter, Depends, HTTPException, status, Path
from sqlalchemy.orm import Session


from ..dependencies import get_db
from ..schemas.fact_schema import FactOut
from ..services import fact_service

router = APIRouter(prefix="/facts",
                   tags=['Facts'],
                   dependencies=[Depends(get_db)])


@router.get(path="/", response_model=list[FactOut], status_code=status.HTTP_200_OK)
def get_facts(db: Session = Depends(get_db)):
    facts = fact_service.get_facts(db=db)
    return facts


@router.get(path="/{fact_id}", response_model=FactOut, status_code=status.HTTP_200_OK)
def get_fact_detail(fact_id: int = Path(..., gt=0, example=1), db: Session = Depends(get_db)):
    fact = fact_service.get_fact(db, fact_id)
    if fact is None:
        raise HTTPException(status_code=404, detail="Fact Not found")
    return fact

@ router.post(path="/", status_code=status.HTTP_201_CREATED)
def create_fact():
    pass


@ router.delete(path="/{fact_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_fact(fact_id: int = Path(..., gt=0, example=1)):
    return {"fat_id": fact_id}
