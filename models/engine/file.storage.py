#!/usr/bin/python3

import json
import os

from models.base_model import BaseModel
""""""

class FileStorage:
    __file_path = "file.json"
    __objects={}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__object[key] = obj

    def save(self):

        list_obj = [to_dictionary(o) for o in __object]

        try:
            for data in list_obj
                with open(FileStorage.__file_path, "w") as file:
                    json.dump(data, file)
        except FileNotFoundError:
            return {}


    def reload(self):
        if os.path.exits(_file_path):
            with open(FileStorage.__file_path, "r") as file:
                data=json.loads(file)
                for o in data.values():








    

