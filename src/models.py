import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, ARRAY
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class MyUser(Base):
    __tablename__ = 'my_user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False) 
    email = Column(String(250), unique=True, nullable=False)
    password = Column(String(250), nullable=False)
    favorites = relationship('favorites')

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), unique=True, nullable=False)
    status = Column(String(250))
    species = Column(String(250), nullable=False)
    favorites = relationship('favorites')

    # person_id = Column(Integer, ForeignKey('person.id'))
    # person = relationship(Person)

class Episode(Base):
    __tablename__ = 'episode'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), unique=True, nullable=False)
    air_date = Column(String(250), nullable=False)
    characters = Column(ARRAY(String(250)))
    favorites = relationship('favorites')

class Location(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), unique=True, nullable=False)
    dimension = Column(String(250))
    type = Column(String(250), nullable=False)
    favorites = relationship('favorites')

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('my_user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    episode_id = Column(Integer, ForeignKey('episode.id'))
    location_id = Column(Integer, ForeignKey('location.id'))
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
