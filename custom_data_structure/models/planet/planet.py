from typing import Optional
from models.abstractmodel import AbstractModel


class PlanetModel(AbstractModel):
    id: int
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
