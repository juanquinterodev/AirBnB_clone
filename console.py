#!/usr/bin/python3

import cmd
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ HBNB class """

    prompt = '(hbnb) '

    def do_quit(self, inp):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, inp):
        """End of File - ctrl + D"""
        return True

    def emptyline(self):
        """Empty line do anything"""
        return False

    def do_create(self, inp):
        inp = shlex.split(inp)
        if inp == []:
            print("** class name missing **")
        elif inp[0] not in ["BaseModel", "User", "Place", "State",
                            "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
        else:
            classes = {"Amenity": Amenity,
                       "BaseModel": BaseModel,
                       "City": City,
                       "Place": Place,
                       "Review": Review,
                       "State": State,
                       "User": User}
            models.storage.reload()
            new = classes[inp[0]]()
            new.save()
            print(new.id)

    def do_all(self, inp):
        inp = shlex.split(inp)
        if inp == []:
            models.storage.reload()
            all_objects = []
            for key, value in models.storage.all().items():
                all_objects.append(value.__str__())
            print(all_objects)
        elif inp[0] not in ["BaseModel", "User", "Place", "State",
                            "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
        else:
            models.storage.reload()
            all_objects = []
            for key, value in models.storage.all().items():
                if value.__class__.__name__ == inp[0]:
                    all_objects.append(value.__str__())
            print(all_objects)

    def do_show(self, inp):
        inp = shlex.split(inp)
        if inp == []:
            print("** class name missing **")
        elif inp[0] not in ["BaseModel", "User", "Place", "State",
                            "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            models.storage.reload()
            for key, value in models.storage.all().items():
                if value.id == inp[1] and value.__class__.__name__ == inp[0]:
                    print(value.__str__())
                    return
            print("** no instance found **")

    def do_destroy(self, inp):
        inp = shlex.split(inp)
        if inp == []:
            print("** class name missing **")
        elif inp[0] not in ["BaseModel", "User", "Place", "State",
                            "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
        elif len(inp) == 1:
            print("** instance id missing **")
        else:
            models.storage.reload()
            all_objects = models.storage.all()
            for key, value in all_objects.items():
                if value.id == inp[1] and value.__class__.__name__ == inp[0]:
                    del(all_objects[key])
                    models.storage.save()
                    return
            print("** no instance found **")

    def do_update(self, inp):
        inp = shlex.split(inp)
        if inp == []:
            print("** class name missing **")
        elif inp[0] not in ["BaseModel", "User", "Place", "State",
                            "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
        elif len(inp) == 1:
            print("** instance id missing **")
        else:
            models.storage.reload()
            all_objects = models.storage.all()
            for key, value in all_objects.items():
                if value.id == inp[1] and value.__class__.__name__ == inp[0]:
                    if len(inp) == 2:
                        print("** attribute name missing **")
                        return
                    elif len(inp) == 3:
                        print("** value missing **")
                        return
                    else:
                        new_inp = inp[3]
                        if hasattr(value, str(inp[2])):
                            new_inp = (type(getattr(value, inp[2])))(inp[3])
                        value.__dict__[inp[2]] = new_inp
                        models.storage.save()
                        return
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
