#!/usr/bin/python3
"""The City Class"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Represents a City Class"""
    city = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guests = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity = []
