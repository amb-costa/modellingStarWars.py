import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

#basic model: diagram for a single user
#one user has a unique favorite table: one to one
#main favorite has branches to every secondary favorite, which is unique to the main favorite: one to one
#many elements can go into an unique secondary favorite: one to many

#User: should login
#That implies it has a username, registered email, and a password
#also linked to their favorites through an ID: fav_id
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    fav_id = Column(Integer, ForeignKey("favorites.id"))
    favorites = relationship("Favorites")

 
#Character: same as the SWAPI exercise. Not person, since there's other races on the universe
#name, birth year, homeworld, gender, height, mass
#keep in mind: birth year should be a string: BBY/ABY (before/after the battle of Yavin)
#connected to a secondary favorite table
class Character(Base):
    __tablename__ = "character"
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    birth_year = Column(String(250))
    homeworld = Column(String(250))
    gender = Column(String(250))
    height = Column(Integer)
    mass = Column(Integer)
    isfav = Column(Boolean)
    #it's possible to establish a relationship between homeworld and the planets database

#CharFavorite: exclusive table to store id of characters with isfav=true
class CharFavorite(Base):
    __tablename__= "charfav"
    id = Column(Integer, primary_key=True)
    favid = Column(Integer, ForeignKey("character.filter_by(isfav=True)"))
    character = relationship(Character)

#Planet: same as the SWAPI exercise
#name, population, diameter, orbital period, rotation period, gravity
class Planet(Base):
    __tablename__ = "planet"
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    population = Column(Integer)
    diameter = Column(Integer)
    orbital_period = Column(Integer)
    rotation_period = Column(Integer)
    gravity = Column(Integer)
    isfav = Column(Boolean)

#PlanFavorite: exclusive table to store id of planets with isfav=true
class PlanFavorite(Base):
    __tablename__ = "planfav"
    id = Column(Integer, primary_key=True)
    favid = Column(Integer, ForeignKey("planet.filter_by(isfav=True)"))
    planet = relationship(Planet)


#Vehicle: same as the SWAPI exercise
#name, model, vehicle class, crew, passengers, cargo capacity
class Vehicle(Base):
    __tablename__ = "vehicle"
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    vehicle_model = Column(String(250))
    vehicle_class = Column(String(250))
    crew_capacity = Column(Integer)
    passenger_capacity = Column(Integer)
    cargo_capacity = Column(Integer)
    isfav = Column(Boolean)

#VehicFavorite: exclusive table to store id of vehicles with isfav=true
class VehicFavorite(Base):
    __tablename__ = "vehicfav"
    id = Column(Integer, primary_key=True)
    favid = Column(Integer, ForeignKey("vehicle.filter_by(isfav=True)"))
    vehicle = relationship(Vehicle)

#Starship: not the same as vehicle: has hyperdrive capability
#name, model, manufacturer, hyperdrive_rating (as hyperdrive), max_atmosphering_speed (at max_atm)
#rating could include a decimal (4.0), max_atm could be N/A if the starship is incapable of atmospheric flight
class Starship(Base):
    __tablename__ = "starship"
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    model = Column(String(250))
    manufacturer = Column(String(250))
    hyperdrive = Column(String(250))
    max_atm = Column(String(250))
    isfav = Column(Boolean)

#StarshFavorite: exclusive table to store id of starships with isfav=true
class StarshFavorite(Base):
    __tablename__ = "starshfav"
    id = Column(Integer, primary_key=True)
    favid = Column(Integer, ForeignKey("starship.filter_by(isfav=True)"))
    starship = relationship(Starship)

#Favorites: user should store their favorites
#condenses all of the secondary favorite tables
#exclusive to a single user
class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    char_id = Column(Integer, ForeignKey("charfav.id"))
    plan_id = Column(Integer, ForeignKey("planfav.id"))
    vehic_id = Column(Integer, ForeignKey("vehicfav.id"))
    starsh_id = Column(Integer, ForeignKey("starshfav.id"))
    charfav = relationship(CharFavorite)
    planfav = relationship(PlanFavorite)
    vehicfav = relationship(VehicFavorite)
    starshfav = relationship(StarshFavorite)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
