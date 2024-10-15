from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from ....dependencies import database

class Card(database.Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    attack = Column(Integer)
    health = Column(Integer)
    description = Column(String)
    speed = Column(Float)
    range = Column(Float)
