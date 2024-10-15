from pydantic import BaseModel
from typing import List

class CardCreate(BaseModel):
    name: str
    attack: int
    health: int
    description: str
    speed: float
    range: float

class CardResponse(CardCreate):
    id: int

    class Config:
        orm_mode = True
