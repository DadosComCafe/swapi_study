from typing import Optional
from pydantic import BaseModel


class PlanetModel(BaseModel):
    name: str
    rotation_period: Optional[str] = None
    orbital_period: Optional[str] = None
    diameter: Optional[str] = None
    climate: Optional[str] = None
    gravity: Optional[str] = None
    terrain: Optional[str] = None
    surface_water: Optional[str] = None
    population: Optional[str] = None
    residents: Optional[list] = []
    films: Optional[list] = []
    created: Optional[str] = None
    edited: Optional[str] = None
    url: Optional[str] = None
