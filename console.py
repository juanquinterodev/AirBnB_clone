#!/usr/bin/python3
import cmd, sys

class HBNBCommand(cmd.Cmd):
    prompt = '(hnbn) '
    file = None
    def do_quit(self, inp):
        print("bye")
        return True
    def help_quit(self):
        print('Quit command to exit the program')
    do_EOF = do_quit
    help_EOF = help_quit
"""quit
EOF
do_help()
emptyline
"""
if __name__ == "__main__":
    HBNBCommand().cmdloop()
