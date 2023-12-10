#!/usr/bin/python3
"""The User Module"""

from models.base_model import BaseModel


class User(BaseModel):
    """Represents a User Class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
