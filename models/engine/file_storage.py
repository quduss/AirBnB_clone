#!/usr/bin/python3
"""FileStorage class definition"""

from ..base_model import BaseModel
import json


class FileStorage:
    """FileStorage class"""
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """initialising instance of FileStorage"""
        pass

    def all(self):
        """return __objects dictionary that contains all instances"""
        return type(self).__objects

    def new(self, obj):
        """Adds a new instance that has been created to
        the __objects dictionary"""
        key = f"{type(obj).__name__}.{obj.id}"
        my_dict = type(self).__objects
        my_dict[key] = obj

    def save(self):
        """serialises __objects dictionary to a json file"""
        my_dict = type(self).__objects
        convert_dict = my_dict.copy()
        for key in convert_dict.keys():
            obj = convert_dict[key]
            obj_json = obj.to_dict()
            convert_dict[key] = obj_json
        with open(type(self).__file_path, 'w', encoding='utf-8') as a_file:
            json.dump(convert_dict, a_file)

    def reload(self):
        """deserialise the json file back to the __objects dictionary"""
        try:
            with open(type(self).__file_path, 'r', encoding='utf-8') as a_file:
                convert_dict = json.load(a_file)
            for key in convert_dict.keys():
                obj_json = convert_dict[key]
                obj = BaseModel(**obj_json)
                convert_dict[key] = obj
            type(self).__objects = convert_dict
        except FileNotFoundError:
            pass
