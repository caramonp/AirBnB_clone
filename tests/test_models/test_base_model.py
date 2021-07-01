#!/usr/bin/python3
"""[Unittest file for BaseModel class]
"""


import unittest
from models.base_model import BaseModel
from uuid import uuid4
from datetime import datetime
import json


class testBaseModel(unittest.TestCase):
    """[Class testBaseModel to test the BaseModel Class]
    """
    def test_kwargs(self):
        """[Test for kwargs as attributes values]
        """
        obj = BaseModel()
        obj.name = "Holberton"
        obj.my_number = 89
        _json = obj.to_dict()

        obj2 = BaseModel(**_json)

        self.assertIsInstance(obj2, BaseModel)
        self.assertIsInstance(_json, dict)
        self.assertIsNot(obj, obj2)

    def test_doc_module(self):
        """[Module documentation]
        """
        doc = BaseModel.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_base_model(self):
        """[Test that models/base_model.py conforms to PEP8]
        """
        _pep8 = pep8.StyleGuide(quiet=True)
        result = _pep8.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """[Constructor documentation]
        """
        doc = BaseModel.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_types_BaseModel(self):
        """[test for all the types in BaseModel class]
        """
        my_model = BaseModel()
        self.assertIs(type(my_model), BaseModel)
        my_model.name = "Holberton"
        my_model.my_number = 89
        self.assertEqual(my_model.name, "Holberton")
        self.assertEqual(my_model.my_number, 89)
        model_types_json = {
            "my_number": int,
            "name": str,
            "__class__": str,
            "updated_at": str,
            "id": str,
            "created_at": str
            }

    def test_uuid_BaseModel(self):
        """[testing different id using uuid]
        """
        model = BaseModel()
        model_2 = BaseModel()
        self.assertNotEqual(model.id, model_2.id)

    def test_datetime_BaseModel(self):
        """[testing different datetime base model]
        """
        model_3 = BaseModel()
        model_4 = BaseModel()
        self.assertNotEqual(model_3.created_at, model_4.updated_at)

    def test_string_representation(self):
        """[Test if the output is a str]
        """
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        id_model = my_model.id

    def test_save(self):
            """[Test for is saved to file]
            """
            base_save = BaseModel()
            base_save.save()
            with open("file.json", 'r') as f:
                self.assertIn(base_save.id, f.read())

    if __name__ == '__main__':
        unittest.main()
        """
        my_model = BaseModel()
        self.assertIs(type(my_model), BaseModel)
        my_model.name = "Holberton"
        my_model.my_number = 89
        self.assertEqual(my_model.name, "Holberton")
        self.assertEqual(my_model.my_number, 89)
        model_types_json = {
            "my_number": int,
            "name": str,
            "__class__": str,
            "updated_at": str,
            "id": str,
            "created_at": str
        }

    def test_uuid_BaseModel(self):
        """[testing different id using uuid]
        """
        model = BaseModel()
        model_2 = BaseModel()
        self.assertNotEqual(model.id, model_2.id)

    def test_datetime_BaseModel(self):
        """[testing different datetime base model]
        """
        model_3 = BaseModel()
        model_4 = BaseModel()
        self.assertNotEqual(model_3.created_at, model_4.updated_at)

    def test_string_representation(self):
        """[Test if the output is a str]
        """
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        id_model = my_model.id

    def test_save(self):
        """[Test for is saved to file]
        """
        base_save = BaseModel()
        base_save.save()
        with open("file.json", 'r') as f:
            self.assertIn(base_save.id, f.read())

if __name__ == '__main__':
    unittest.main()
