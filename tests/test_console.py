#!/usr/bin/python3
"""Unittest cases for console"""

import unittest
from unittest.mock import patch
import console
from console import HBNBCommand
from io import StringIO
import pep8
import sys


class Test_BaseModel(unittest.TestCase):
    """ """

    def test_help(self):
        """  """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            cont_EOF = f.getvalue()
            HBNBCommand().onecmd("help quit")
            cont_quit = f.getvalue()
            HBNBCommand().onecmd("help all")
            cont_all = f.getvalue()
            HBNBCommand().onecmd("help create")
            cont_create = f.getvalue()
            HBNBCommand().onecmd("help destroy")
            cont_destroy = f.getvalue()
            HBNBCommand().onecmd("help help")
            cont_help = f.getvalue()
            HBNBCommand().onecmd("help show")
            cont_show = f.getvalue()
            HBNBCommand().onecmd("help update")
            cont_update = f.getvalue()
        self.assertNotEqual(cont_EOF, "*** No help on EOF\n")
        self.assertNotEqual(cont_quit, "*** No help on quit\n")
        self.assertNotEqual(cont_all, "*** No help on all\n")
        self.assertNotEqual(cont_create, "*** No help on create\n")
        self.assertNotEqual(cont_destroy, "*** No help on destroy\n")
        self.assertNotEqual(cont_help, "*** No help on help\n")
        self.assertNotEqual(cont_show, "*** No help on show\n")
        self.assertNotEqual(cont_update, "*** No help on update\n")
