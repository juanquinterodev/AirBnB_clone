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
        elif len(inp) == 1:
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

    def commands(self, inp):
        """command capture"""
        args = str(inp).split('.')
        if not args[0] in ["BaseModel", "User", "Place", "State",
                           "City", "Amenity", "Review"]:
           print("unknown syntax")
        else:
             if args[1] == "all()":
                self.do_all(args[0])

             elif args[1] == "count()":
                 objects = models.storage.all()
                 count = 0
                 for key, value in objects.items():
                     name = str(key).split('.')
                     if args[0] == name[0]:
                         count += 1
                 print(cont)
             
             elif "show(" in args[1]:
                 line = args[1].replace("show(", "")
                 line = line[:-1]
                 val = "{} {}".format(args[0], line)
                 self.do_show(val)

             elif "destroy(" in args[1]:
                 line = args[1].replace("destroy(", "")
                 line = line[:-1]
                 val = "{} {}".format(args[0], line)
                 self.do_destroy(val)

             elif "update(" in args[1]:
                 line = args[1].replace("update(", "")
                 line = line[:-1]
                 todict = line[:]
                 arg = line.split(',')
                 sid = arg[0][1:-1]
                 val = args[0] + " "
                 if arg[1][1] == '{':
                       arg = todict.split(',', 1)
                       dic = eval(arg[1][1:])
                       dic['id'] = sid
                       objects = models.storage.all()
                       key = "{}.{}".format(args[0], sid)
                       if key in objects:
                           obj = models.storage.classes[args[0]](**dic)
                           objects[key] = obj
                           obj.save()
                       else:
                           print("** no instance found **")

                 else:
                     count = 0
                     for value in arg:
                         if count == 2:
                             value = ' "' + value[1:] + '"'
                             value = value + v
                             count += 1
                     self.do_update(value)

             else:
                 print("*** Unknown syntax: {}".format(inp))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
