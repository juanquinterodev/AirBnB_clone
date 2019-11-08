#!/usr/bin/python3
import cmd, sys

class HBNBCommand(cmd.Cmd):
    prompt = '(hnbn) '
    file = None
    def do_quit(self, inp):
        print("bye")
        return True
    do_EOF = do_quit
"""quit
EOF
do_help()
emptyline
"""
if __name__ == "__main__":
    HBNBCommand().cmdloop()
