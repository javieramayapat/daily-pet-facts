from sqlalchemy.orm import Session

from ..models.models import Pet


def get_pets(db: Session):
    return db.query(Pet).all()


def get_pet(db: Session, pet_id: int):
    return db.query(Pet).filter(Pet.id == pet_id).first()
