#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py."""
from models.engine.file_storage import FileStorage
import unittest
import pep8
import json
import os
from models.user import User
from models.base_model import BaseModel
from models import storage


class TestFileStorage(unittest.TestCase):
    """Testing instantiation of the FileStorage class."""
    storage = FileStorage()
    path = storage._FileStorage__file_path

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_pep8_base(self):
        """ test pep8 style"""
        self.assertEqual(os.system('pep8 models/engine/file_storage.py'), 0)

    def test_module_docstring(self):
        """test documentation"""
        self.assertTrue(len(FileStorage.__doc__) > 1)
        self.assertTrue(len(FileStorage.__init__.__doc__) > 1)
        self.assertTrue(len(FileStorage.all.__doc__) > 1)
        self.assertTrue(len(FileStorage.new.__doc__) > 1)
        self.assertTrue(len(FileStorage.save.__doc__) > 1)
        self.assertTrue(len(FileStorage.reload.__doc__) > 1)

    def test_name_file(self):
        """teste name module"""
        self.assertTrue(hasattr(FileStorage, "__init__"))
        self.assertTrue(hasattr(FileStorage, "all"))
        self.assertTrue(hasattr(FileStorage, "new"))
        self.assertTrue(hasattr(FileStorage, "save"))
        self.assertTrue(hasattr(FileStorage, "reload"))

    def test_all(self):
        """test all dictionary"""
        storage = FileStorage()
        self.assertEqual(type(storage.all()), dict)
        self.assertIs(storage.all(), storage._FileStorage__objects)

    def test_new(self):
        """test new creation"""
        storage = FileStorage()
        obj = storage.all()
        user = User()
        user.id = "0123"
        user.name = "Holberton"
        storage.new(user)
        self.assertIsNotNone(obj[user.__class__.__name__ + "." + user.id])
        self .assertEqual(obj[user.__class__.__name__ + "." + user.id], user)
        try:
            self.assertRaises(storage.new(None), TypeError)
        except:
            pass

    def test_save(self):
        """test save"""
        storage = FileStorage()
        storage.save()
        self.assertTrue(os.path.exists("file.json"))
        test = BaseModel()
        test.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_save_another_instance(self):
        """
        Tests for save another instance in path
        """
        bm2_instance = BaseModel()
        bm2_instance.save()
        key = type(bm2_instance).__name__ + "." + str(bm2_instance.id)
        with open(TestFileStorage.path, mode="r", encoding="utf-8") as f:
            reader = json.load(f)
        self.assertEqual(
            reader[key], TestFileStorage.storage.all()[key].to_dict())

    def test_save_another_instance(self):
        """
        Tests for save another instance in path
        """
        bm2_instance = BaseModel()
        bm2_instance.save()
        key = type(bm2_instance).__name__ + "." + str(bm2_instance.id)
        with open(TestFileStorage.path, mode="r", encoding="utf-8") as f:
            reader = json.load(f)
        self.assertEqual(
            reader[key], TestFileStorage.storage.all()[key].to_dict())

if __name__ == '__main__':
    pass
