#!/usr/bin/python3
""" Base Model Module"""

from uuid import uuid4
from datetime import datetime


class BaseModel():
    """ Base Model class """
    id
    created_at = datetime.now()
    update_at = datetime.now()

    def __init__(self, *args, **kwargs):
        """Constructor"""
        self.id = str(uuid4())
        for key, value  in kwargs.items():
            if key is "created_at":
                self.created_at = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
            elif key is "update_at":
                self.update_at = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
            elif key is "id":
                self.id = value
            elif key is "name":
                self.name = value
            elif key is "my_number":
                self.my_number = value
	

    def __str__(self):
        """str should print class name, id, dict"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)


    def save(self):
        """Save funct"""
        self.update_at = datetime.now()


    def to_dict(self):
        """To dict funct"""
        class_dict = self.__dict__.copy()
        class_dict.update({'__class__': self.__class__.__name__})
        class_dict.update({'created_at': self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")})
        class_dict.update({'update_at': self.update_at.strftime("%Y-%m-%dT%H:%M:%S.%f")})
        return class_dict
