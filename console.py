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

    def do_quit(self, inp):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, inp):
        """ End of File - ctrl + D """
        return True

    def emptyline(self):
        """ Empty line do anything """
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
