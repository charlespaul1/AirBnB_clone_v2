#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    cities = relationship("City", cascade="all, delete, delete-orphan")

    @property
    def cities(self):
        from models import storage
        cities = storage.all("City").values()
        return [city for city in cities if city.state_id == self.id]
