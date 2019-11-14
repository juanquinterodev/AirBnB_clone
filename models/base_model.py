#!/usr/bin/python3
""" Base Model Module"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """ Base Model class """
    id
    created_at = datetime.now()
    updated_at = datetime.now()

    def __init__(self, *args, **kwargs):
        """Constructor"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs  is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key is "created_at":
                    date_iso = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    self.created_at = date_iso
                elif key is "update_at":
                    date_iso = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    self.updated_at = date_iso
                elif key is "id":
                    self.id = value
                elif key is "name":
                    self.name = value
                elif key is "my_number":
                    self.my_number = value
            models.storage.new(self)

    def __str__(self):
        """str should print class name, id, dict"""
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        return "[{}] ({}) {}".format(class_name, self.id, class_dict)

    def save(self):
        """Save funct"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """To dict funct"""
        class_dict = self.__dict__.copy()
        created_at_string = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        updated_at_string = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        class_dict.update({'__class__': self.__class__.__name__})
        class_dict.update({'created_at': created_at_string})
        class_dict.update({'updated_at': updated_at_string})
        return class_dict

