#!/usr/bin/python3

import cmd
import models
from models.base_model import BaseModel
import shlex

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
        """ create instances"""
        args = str(inp).split(' ')
        if len(inp) == 0:
            print("** class name missing **")
        elif not args[0] in models.storage.classes:
            print("** class doesn't exist **")
        else:
            my_model = models.storage.classes[args[0]]()
            my_model.save()
            print(my_model.id)

    def do_all(self, inp):
        """ all instances """
        args = str(inp).split(' ')
        objects = models.storage.all()
        alls = []
        if args[0] == "":
            for key, value in objects.items():
                alls.append(str(value))
            print(alls)
        elif not args[0] in models.storage.classes:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                name = str(key).split('.')
                if args[0] == name[0]:
                    alls.append(str(value))
            print(alls)

    def do_show(self, inp):
        """ Show instance """
        args = str(inp).split(' ')
        showid = 0
        if args[0] == '':
            print("** class name missing **")
        elif not args[0] in models.storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = models.storage.all()
            try:
                obj = objects["{}.{}".format(args[0], args[1])]
                print(obj)
            except:
                print("** no instance found **")

    def do_destroy(self, inp):
        """ delete instance """
        if not inp:
            args = ['']
        else:
            args = shlex.split(inp)
        showid = 0
        if args[0] == '':
            print("** class name missing **")
        elif not args[0] in models.storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = models.storage.all()
            try:
                key = "{}.{}".format(args[0], args[1])
                obj = objects[key]
                del objects[key]
                models.storage.save()
            except:
                print("** no instance found **")

    def do_update(self, inp):
        """ update instance """
        if not inp:
            args = ['']
        else:
            args = shlex.split(inp)
        showid = 0
        if args[0] == '':
            print("** class name missing **")
        elif not args[0] in models.storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            try:
                obj = models.storage.all().get(key)
                setattr(models.storage.all()[key], args[2], args[3])
                models.storage.save()
            except:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
