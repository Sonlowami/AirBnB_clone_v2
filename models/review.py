#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = 'reviews'
    place_id = Column(String(128), ForeignKey('Place'), nullable=False)
    user_id = Column(String(128), ForeignKey('User'), nullable=False)
    text = Column(String(1024), nullable=False)
