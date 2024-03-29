import json
from pathlib import Path
from ..base_model import BaseModel
from ..amenity import Amenity
from ..city import City
from ..place import Place
from ..state import State
from ..user import User
from ..review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects.update({key: obj})

    def save(self):
        with open(self.__file_path, 'w') as outfile:
            new_obj = {}
            for key, value in self.__objects.items():
                new_obj.update({key: value.to_dict()})
            json.dump(new_obj, outfile)

    def reload(self):
        classes = {"Amenity": Amenity,
                   "BaseModel": BaseModel,
                   "City": City,
                   "Place": Place,
                   "Review": Review,
                   "State": State,
                   "User": User}
        my_file = Path(self.__file_path)
        if my_file.is_file():
            with open(self.__file_path) as json_file:
                loads = json.load(json_file)
                for key, value in loads.items():
                    obj = classes[value["__class__"]](**value)
                    self.__objects.update({key: obj})
