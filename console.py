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

    def help_quit(self):
        """ Update help cmd """
        print('Quit command to exit the program')

    do_EOF = do_quit
    """End of File - ctrl + D"""

    help_EOF = help_quit
    """ Update help quit - EOF """

    def unknown(self, inp):
        """ Default command """
        try:
            self.onecmd(eval(inp))
        except:
            print("Unknown: " + inp)

    def emptyline(self):
        """ Empty line do anything """
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
