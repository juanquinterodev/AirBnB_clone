#!/usr/bin/python3
"""
Unit test for the Base class
"""

import unittest
import json
import os
import pep8
from models.base_model import BaseModel

class TestBase(unittest.TestCase):
    """
    Test cases for the Base class
    """

    def test_docstring(self):
        """
        Testing docstring
        """
        self.assertIsNotNone(BaseModel.__doc__)

    def test_documentation(self):
        """
        Test to see if documentation is correct and created
        """
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(BaseModel.__init__.__doc__)
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(BaseModel.__str__.__doc__)
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(BaseModel.save.__doc__)
        self.assertTrue(hasattr(Base, "to_dict"))
        self.assertTrue(Base.to_dic.__doc__)

    def test_pep8_conformance(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "Fix PEP8")

    def test_base_creation(self):
        """
        Testing the creation of the base
        """
        b = Base()
        test = str(b)
        b1 = Base(12)
        test1 = str(b1)
        b2 = Base()
        test2 = str(b2)
        self.assertTrue(test[:29], '<models.base_model.BaseModel object at ')
        self.assertTrue(b.id, 1)
        self.assertTrue(test1[:29], '<models.base_model.BaseModel object at ')
        self.assertTrue(b1.id, 12)
        self.assertTrue(test2[:29], '<models.base_model.BaseModel object at ')
        self.assertTrue(b2.id, 2)

    def test_base_instance(self):
        b = BaseModel()
        self.assertIsInstance(b, BaseModel)
