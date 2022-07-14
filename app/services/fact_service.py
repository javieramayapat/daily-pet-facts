from sqlalchemy.orm import Session

from ..models import Fact


def get_facts(db: Session):
    return db.query(Fact).all()


def get_fact(db: Session, fact_id: int):
    return db.query(Fact).filter(Fact.id == fact_id).first()
