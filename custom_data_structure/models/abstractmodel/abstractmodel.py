from typing import Optional
from pydantic import BaseModel


class AbstractModel(BaseModel):
    id: int
    name: str
    created: Optional[str] = None
    edited: Optional[str] = None
    url: Optional[str] = None
