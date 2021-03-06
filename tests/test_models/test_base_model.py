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
        self.assertTrue(hasattr(model, "id"))

    def test_datetime_BaseModel(self):
        """[testing different datetime base model]
        """
        model_3 = BaseModel()
        model_4 = BaseModel()
        self.assertNotEqual(model_3.created_at, model_4.updated_at)

    def test_string_representation(self):
        """[Test if the output is a str]
        """
        basemodel1 = BaseModel()
        printed = "[{}] ({}) {}".format(
            basemodel1.__class__.__name__, basemodel1.id, basemodel1.__dict__)
        self.assertEqual(str(basemodel1), printed)

    def test_save(self):
        """[Test for is saved to file]
        """
        base_save = BaseModel()
        base_save.save()
        with open("file.json", 'r') as f:
            self.assertIn(base_save.id, f.read())
        date1 = base_save.updated_at
        base_save.save()
        self.assertNotEqual(date1, base_save.updated_at)

    def test_to_dict(self):
        """Test the to_dict method from BaseModel"""
        basemodel1 = BaseModel()
        basemodel1_dict = basemodel1.to_dict()
        self.assertIsInstance(basemodel1_dict, dict)
        self.assertEqual(basemodel1_dict["__class__"], "BaseModel")
        self.assertEqual(str(basemodel1.id), basemodel1_dict["id"])
        self.assertIsInstance(basemodel1_dict["created_at"], str)
        self.assertIsInstance(basemodel1_dict["updated_at"], str)

if __name__ == '__main__':
    unittest.main()
