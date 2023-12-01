from typing import Optional
from models.abstractmodel import AbstractModel
from models.starship import StarShipModel
from models.planet import PlanetModel


class PersonModel(AbstractModel):
    height: Optional[str] = None
    mass: Optional[str] = None
    hair_color: Optional[str] = None
    skin_color: Optional[str] = None
    eye_color: Optional[str] = None
    birth_year: Optional[str] = None
    gender: Optional[str] = None
    homeworld: Optional[PlanetModel] = None
    films: Optional[list[str]] = []
    species: Optional[list[str]] = []
    vehicles: Optional[list[str]] = []
    starships: Optional[list[StarShipModel]] = []
    created: Optional[str] = None
    edited: Optional[str] = None
    url: Optional[str] = None
