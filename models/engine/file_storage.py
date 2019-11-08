import json
from pathlib import Path

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects = obj

    def save(self):
        with open(self.__file_path, 'a') as outfile:
            key = self.__objects.__class__.__name__ + "." + self.__objects.id
            print(key)
            json.dump({key: self.__objects.to_dict()}, outfile)

    def reload(self):
        my_file = Path("file.json")
        if my_file.is_file():
            with open(self.__file_path) as json_file:
                return json.load(json_file)
