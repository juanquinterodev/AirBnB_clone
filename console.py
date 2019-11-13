#!/usr/bin/python3
""" Console Module"""

import cmd
import sys
import models
from models.user import User
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ HBNB class """

    prompt = '(hnbn) '
    file = None

    def do_quit(self, inp):
        """ Exit command """
        return True

    def do_EOF(self):
        """ End of File - ctrl + D """
        return False

    def emptyline(self):
        """ Empty line do anything """
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
