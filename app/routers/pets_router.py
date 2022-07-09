from fastapi import APIRouter, status

router = APIRouter(prefix="/pets", tags=["Pets"])


@router.get(path="/", status_code=status.HTTP_200_OK)
def get_pet_types():
    pass
