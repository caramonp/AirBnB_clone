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
  
  
if __name__ == '__main__':
    unittest.main()