#!/usr/bin/python3
""" Base Model Module"""

from uuid import uuid4
from datetime import datetime


class BaseModel():
    """ Base Model class """
    id
    created_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
    update_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")

    def __init__(self):
        """Constructor"""
        self.id = str(uuid4())


    def __str__(self):
        """str should print class name, id, dict"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)


    def save(self):
        """Save funct"""
        self.update_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")


    def to_dict(self):
        """To dict funct"""
        class_dict = self.__dict__.copy()
        class_dict.update({'__class__': self.__class__.__name__})
        class_dict.update({'created_at': self.created_at})
        class_dict.update({'update_at': self.update_at})
        return class_dict
