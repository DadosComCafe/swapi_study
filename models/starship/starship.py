from typing import Optional
from pydantic import BaseModel

class StarShipModel(BaseModel):
    name: str
    model: Optional[str] = None
    manufacturer: Optional[str] = None
    cost_in_credits: Optional[str] = None
    length: Optional[str] = None
    max_atmosphering_speed: Optional[str] = None
    crew: Optional[str] = None
    passengers: Optional[str] = None
    cargo_capacity: Optional[str] = None
    consumables: Optional[str] = None
    hyperdrive_rating: Optional[str] = None
    MGLT: Optional[str] = None
    starship_class: Optional[str] = None
    pilots: Optional[list] = []
    films: Optional[list] = []
    created: Optional[str] = None
    edited: Optional[str] = None
    url: Optional[str] = None