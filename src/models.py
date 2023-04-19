import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

#User: should login
#That implies it has a username, registered email, and a password
#also linked to their favorites through an ID: user_id

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    fav_id = Column(Integer, ForeignKey("favorites.id" ))
    favorites = relationship("Favorites")

 
#Character: same as the SWAPI exercise. Not person, since there's other races on the universe
#name, birth year, homeworld, gender, height, mass
#keep in mind: birth year should be a string: BBY/ABY (before/after the battle of Yavin)
class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    birth_year = Column(String(250))
    homeworld = Column(String(250))
    gender = Column(String(250))
    height = Column(Integer)
    mass = Column(Integer)

#Planet: same as the SWAPI exercise
#name, population, diameter, orbital period, rotation period, gravity
class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    population = Column(Integer)
    diameter = Column(Integer)
    orbital_period = Column(Integer)
    rotation_period = Column(Integer)
    gravity = Column(Integer)


#Vehicle: same as the SWAPI exercise
#name, model, vehicle class, crew, passengers, cargo capacity
class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    vehicle_model = Column(String(250))
    vehicle_class = Column(String(250))
    crew_capacity = Column(Integer)
    passenger_capacity = Column(Integer)
    cargo_capacity = Column(Integer)

#Favorites: user should store their favorites
#so far: should store characters, planets and vehicles
#user id, character id, planet id, vehicle id
class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    character_id = Column(String(250), ForeignKey('character.id'))
    planet_id = Column(String(250), ForeignKey('planet.id'))
    vehicle_id= Column(String(250), ForeignKey('vehicle.id'))
    character = relationship(Character)
    planet = relationship(Planet)
    vehicle = relationship(Vehicle)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
