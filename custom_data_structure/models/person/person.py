from typing import Optional
from pydantic import BaseModel
from custom_data_structure.models.starship import StarShipModel


class PersonModel(BaseModel):
    name: str
    height: Optional[str] = None
    mass: Optional[str] = None
    hair_color: Optional[str] = None
    skin_color: Optional[str] = None
    eye_color: Optional[str] = None
    birth_year: Optional[str] = None
    gender: Optional[str] = None
    homeworld: Optional[str] = None
    films: Optional[list[str]] = []
    species: Optional[list[str]] = []
    vehicles: Optional[list[str]] = []
    starships: Optional[StarShipModel] = []
    created: Optional[str] = None
    edited: Optional[str] = None
    url: Optional[str] = None
