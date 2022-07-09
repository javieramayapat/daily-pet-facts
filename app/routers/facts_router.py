from fastapi import APIRouter, status, Path


router = APIRouter(prefix="/facts", tags=['Facts'])


@router.get(path="/", status_code=status.HTTP_200_OK)
def get_facts():
    pass


@router.get(path="/{fact_id}", status_code=status.HTTP_200_OK)
def get_fact_detail(fact_id: int = Path(..., gt=0, example=1)):
    return {"fact_id": fact_id}


@router.post(path="/", status_code=status.HTTP_201_CREATED)
def create_fact():
    pass


@router.delete(path="/{fact_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_fact(fact_id: int = Path(..., gt=0, example=1)):
    return {"fat_id": fact_id}
