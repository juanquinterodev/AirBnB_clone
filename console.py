#!/usr/bin/python3

import cmd


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
