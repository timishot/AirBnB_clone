#!/usr/bin/python3
""" defining a parent class that will be uses by other class"""
from uuid import uuid4
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        iso_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if (kwargs) != 0:
            for k , v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    self.__dict__[k] = datetime.strptime(v, iso_format)
                else:
                    self.__dict__[k] = v


    def save(self):
        """ updates the public instance attribute updated_at with the current datetime """
        self.updated_at = datetime.now()


    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict


    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)


