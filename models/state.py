#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_mode, storage
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if storage_mode():
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref = 'state', cascade="all, delete")

    else:
        name = ""
        def get_cities(self):
            """Return all cities with state_id equal to this object's id"""
            cities = []
            [cities.append(item) for item in storage.all(Cities) if item.state_id == self.id]
            return cities
