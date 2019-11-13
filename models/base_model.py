#!/usr/bin/python3
""" Base Model Module"""

from uuid import uuid4
from datetime import datetime
from . import storage


class BaseModel():
    """ Base Model class """
    id
    created_at = datetime.now()
    update_at = datetime.now()

    def __init__(self, *args, **kwargs):
        """Constructor"""
        self.id = str(uuid4())
        for key, value in kwargs.items():
            if key is "created_at":
                date_iso = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                self.created_at = date_iso
            elif key is "update_at":
                date_iso = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                self.update_at = date_iso
            elif key is "id":
                self.id = value
            elif key is "name":
                self.name = value
            elif key is "my_number":
                self.my_number = value
        storage.new(self)

    def __str__(self):
        """str should print class name, id, dict"""
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        return "[{}] ({}) {}".format(class_name, self.id, class_dict)

    def save(self):
        """Save funct"""
        self.update_at = datetime.now()
        storage.save()

    def to_dict(self):
        """To dict funct"""
        class_dict = self.__dict__.copy()
        created_at_string = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        update_at_string = self.update_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        class_dict.update({'__class__': self.__class__.__name__})
        class_dict.update({'created_at': created_at_string})
        class_dict.update({'update_at': update_at_string})
        return class_dict
