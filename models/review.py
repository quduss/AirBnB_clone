#!/usr/bin/python3
"""The City Class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a City Class"""
    place_id = ""
    user_id = ""
    text = ""
