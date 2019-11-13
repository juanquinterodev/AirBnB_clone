#!/usr/bin/python3
"""Unittest cases for BaseModel"""

import uuid
from models.base_model import BaseModel
from models import storage
import os
import pep8
import unittest


class Test_BaseModel(unittest.TestCase):
    """test for class
    """

    def test_pep8_base_model(self):
        """ Test for style """
        style = pep8.StyleGuide(quiet=True)
        new = style.check_files(['models/base_model.py'])
        self.assertEqual(new.total_errors, 0, "Please fix pep8")

    def test_pep8_tests_base(self):
        """ Test for style """
        style = pep8.StyleGuide(quiet=True)
        new = style.check_files(['tests/test_models/test_base_model.py'])
        self.assertEqual(new.total_errors, 0, "Please fix pep8")

    def test_docstring(self):
        """test docstring"""
        self.assertTrue(len(BaseModel.__doc__) > 1)
        self.assertTrue(len(BaseModel.__init__.__doc__) > 1)
        self.assertTrue(len(BaseModel.__str__.__doc__) > 1)
        self.assertTrue(len(BaseModel.save.__doc__) > 1)
        self.assertTrue(len(BaseModel.to_dict.__doc__) > 1)

    def test_isinstance(self):
        """"Test for instance of the class"""
        elm = BaseModel()
        self.assertIsInstance(elm, BaseModel)

    def test_id_v4_uuid(self):
        """Test UUID version"""
        elm = BaseModel()
        test_uuid = uuid.UUID(elm.id, version=4)
        self.assertEqual(str(test_uuid), elm.id, "Error: Different version")

    def test_args(self):
        """Arguments to the instance"""
        b = BaseModel(8)
        self.assertEqual(type(b).__name__, "BaseModel")
        self.assertFalse(hasattr(b, "8"))

    def test_str(self):
        """check Prints"""
        b = BaseModel()
        printb = b.__str__()
        self.assertEqual(printb, "[BaseModel] ({}) {}".format(b.id, b.__dict__))

    def test_save(self):
        """Testing save function"""
        elm = BaseModel()
        elm.save()
        key = "BaseModel.{}".format(elm.id)
        comp = storage._FileStorage__elmects[key]
        self.assertEqual(elm.id, comp.id)
        self.assertTrue(os.path.isfile("file.json"))
        self.assertNotEqual(elm.created_at, elm.updated_at)

    def test_to_dict(self):
        """Tests to_dict function."""
        elm = BaseModel()
        new_dict = elm.__dict__.copy()
        new_dict["__class__"] = elm.__class__.__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        compare = elm.to_dict()
        self.assertDictEqual(new_dict, compare)
