#!/usr/bin/python3
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    prompt = '(hnbn) '
    file = None

    def do_quit(self, inp):
        return True

    def help_quit(self):
        print('Quit command to exit the program')

    def emptyline(self):
        pass

    do_EOF = do_quit
    help_EOF = help_quit


"""quit
EOF
do_help()
emptyline
"""
if __name__ == "__main__":
    HBNBCommand().cmdloop()
