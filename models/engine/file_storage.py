#!/usr/bin/python3

from ..base_model import BaseModel
import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        return type(self).__objects

    def new(self, obj):
        key = f"{type(obj).__name__}.{obj.id}"
        my_dict = type(self).__objects
        my_dict[key] = obj

    def save(self):
        my_dict = type(self).__objects
        convert_dict = my_dict.copy()
        for key in convert_dict.keys():
            obj = convert_dict[key]
            obj_json = obj.to_dict()
            convert_dict[key] = obj_json
        with open(type(self).__file_path, 'w', encoding='utf-8') as a_file:
            json.dump(convert_dict, a_file)

    def reload(self):
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
