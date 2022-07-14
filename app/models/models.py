from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class User:
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    username = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False)
    password = Column(String(50), nullable=False)

    facts = relationship("Facts", back_populates="users")


class Pet:
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

    facts = relationship("Facts", back_populates="pets")


class Fact:
    __tablename__ = "facts"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String(400), nullable=False)
    source = Column(String(200))
    user_id = Column(Integer, ForeignKey("users.id"))
    pet_id = Column(Integer, ForeignKey("pet.id"))

    users = relationship("Users", back_populates="facts")
    pets = relationship("Pets", back_populates="facts")
