#!/usr/bin/python3
""" Unittests Base Model Module"""

import unittest
from datetime import datetime
from models import storage
from models.base_model import BaseModel
import json
import os
import pep8
import uuid


class Test_BaseModel(unittest.TestCase):
    """ Test Base Model Methods """

    def test_assert_stylepep8_base(self):
        """ Test for style model """
        style = pep8.StyleGuide(quiet=True)
        new = style.check_files(['models/base_model.py'])
        self.assertEqual(new.total_errors, 0, "Error pep8 base model")

    def test_assert_stylepep8_testsbase(self):
        """ Test for style tests """
        style = pep8.StyleGuide(quiet=True)
        new = style.check_files(['tests/test_models/test_base_model.py'])
        self.assertEqual(new.total_errors, 0, "Error pep8 tests")

    def test_assert_docstring(self):
        """ Test docstring """
        self.assertTrue(len(BaseModel.__doc__) > 1)
        self.assertTrue(len(BaseModel.__init__.__doc__) > 1)
        self.assertTrue(len(BaseModel.__str__.__doc__) > 1)
        self.assertTrue(len(BaseModel.save.__doc__) > 1)
        self.assertTrue(len(BaseModel.to_dict.__doc__) > 1)
 
    def test_assert_uuid_version(self):
        """Test id unique and UUID version"""
        elm = BaseModel()
        street = BaseModel()
        self.assertNotEqual(elm.id, street.id)
        jason = uuid.UUID(elm.id, version=4)
        self.assertEqual(str(jason), elm.id, "Error: UUID no version 4")

    def test_assert_instn_attr(self):
        """ Test attributes exists """
        a = BaseModel()
        self.assertTrue(hasattr(b0, 'id'))
        self.assertTrue(hasattr(b0, 'created_at'))
        self.assertTrue(hasattr(b0, 'updated_at'))

    def test_assert_instn_defs(self):
        """ Test methods exists """
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "__str__"))
        self.assertTrue(hasattr(BaseModel, "save"))

    def test_assert_is_instance(self):
        """ Test init instance is ok """
        a = BaseModel()
        self.asserIsInstance(a, BaseModel)

    def test_assert_str(self):
        """ Test str method is ok """
        b = BaseModel()
        printb = b.__str__()
        self.assertEqual(printb, "[BaseModel] ({}) {}".format(b.id, b.__dict__))

    def test_assert_save(self):
        """Testing save function"""
        elm = BaseModel()
        elm.save()
        key = "BaseModel.{}".format(elm.id)
        cmp = storage._FileStorage__elmects[key]
        self.assertEqual(elm.id, cmp.id)
        self.assertTrue(os.path.isfile("file.json"))
        self.assertNotEqual(elm.created_at, elm.updated_at)

    def test_assert_to_dict(self):
        """ Test to_dict method """
        a = self.to_dict()
        self.assertIsInstance(a, dict)
        self.assertIsInstance(a['id'], str)
        self.assertIsInstance(a['updated_at'], str)
        self.assertIsInstance(a['created_at'], str)
        self.assertEqual(a['__class__'], self.__class__.__name__)

if __name__ == "__main__":
    unittest.main()
