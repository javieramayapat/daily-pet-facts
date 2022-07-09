from fastapi import APIRouter


router = APIRouter(tags=["Users"])


@router.post(path='/auth/login')
def login():
    pass


@router.post(path='/signup')
def signup():
    pass


@router.get(path='/users/me')
def get_profile():
    pass
