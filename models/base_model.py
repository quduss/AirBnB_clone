#!/usr/bin/python3

"""BaseModel class definition"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """BaseModel class"""
    def __init__(self, *args, **kwargs):
        """initialising BaseModel instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "updated_at" or key == "created_at":
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """string representation of BaseModel instance"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """method to serialise __objects to json file"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """return dictionary representation of instance"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = type(self).__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict

    def set_attribute(self, key, value):
        """method to set a particular attribute with a value for
        an instance"""
        setattr(self, key, value)
