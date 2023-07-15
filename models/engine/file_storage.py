#!/usr/bin/python3

import json
import os

from models.base_model import BaseModel
"""Defines the FileStorage class."""


class FileStorage:
    """Represent an abstracted storage engine.
    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self, obj = None):
        list_obj = [o.to_dictionary() for o in FileStorage.__objects.values()]
        try:
            with open(FileStorage.__file_path, "w") as file:
                json.dump(list_obj, file)
        except FileNotFoundError:
            return []

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                data = json.load(file)
                FileStorage.__object = {
                        key: self.create_instance_from_data(key, obj_data)
                        for key, obj_data in data.items()
                        }
        else:
            # Handle the case when the file doen't exist
            return []

    def create_instance_from_data(self, key, obj_data):
        class_name = obj_data.get('__class__')
        if class_name:
            cls = globals().get(class_name)
            if cls:
                obj = cls(**obj_data)
                return obj
        # Return None if the objrcy creation fails
        return None
