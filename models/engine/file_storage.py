#!/usr/bin/python3

import json
import os

from models.base_model import BaseModel
from models.user import User
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

    def save(self):
        obj_dict = {obj: FileStorage.__objects[obj].to_dict() 
                    for obj in FileStorage.__objects.keys()}
        try:
            with open(FileStorage.__file_path, "w") as file:
                json.dump(obj_dict, file)
        except FileNotFoundError:
            return 

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                obj_dict = json.load(file)
                if isinstance(obj_dict, list):
                    # Handle the case when obj_dict is a list
                    FileStorage.__objects = {}
                else:
                   FileStorage.__objects= {
                        key: self.create_instance_from_data(key, obj_data)
                        for key, obj_data in obj_dict.items()
                        }
        else:
            # Handle the case when the file doen't exist
            return 

    def create_instance_from_data(self, key, obj_data):
        class_name = obj_data.get('__class__')
        if class_name:
            cls = globals().get(class_name)
            if cls:
                obj = cls(**obj_data)
                return obj
        # Return None if the objrcy creation fails
        return None
