import json
from pathlib import Path

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj.to_dict()

    def save(self):
        with open(self.__file_path, 'w') as outfile:
            json.dump(self.__objects, outfile)

    def reload(self):
        my_file = Path(self.__file_path)
        if my_file.is_file():
            with open(self.__file_path) as json_file:
                self.__objects = json.load(json_file)
                return self.__objects
        else:
            return None
