import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)
    population = Column(Integer)
    gravity = Column(String(40))
    climate = Column(String(50))
    pic = Column(String(500))
    url = Column(String(100))


    def to_dict(self):
        return {}
    
class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    homeworld = Column(String(50), ForeignKey(Planet.name))
    eye_color = Column(String(10))
    gender = Column(String(15))
    hair_color = Column(String(20))
    height = Column(Integer)
    skin_color = Column(String(20))
    pic = Column(String(500))
    url = Column(String(100))

    def to_dict(self):
        return {}

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(40), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)


    def to_dict(self):
        return {}


class Favorites(Base):
    __tablename__ = 'favorites'
    user_id = Column(Integer, ForeignKey(User.id))
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    planet_name = Column(String(40), ForeignKey(Planet.name))
    person_name = Column(String(25), ForeignKey(Person.name))

    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')