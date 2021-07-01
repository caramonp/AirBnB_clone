#!/usr/bin/python3
""" test State """

import unittest
import models
import os
from models.state import State


class TestState(unittest.TestCase):
    """ Test class State"""

    # def test_pep8(self):
    #     """ test pep8 style"""
    #     self.assertEqual(os.system('pep8 models/state.py'), 0)

    def test_module_docstring(self):
        """test documentation"""
        self.assertTrue(len(State.__doc__) >= 1)
        self.assertTrue(len(State.__init__.__doc__) >= 1)

    def test_name_file(self):
        """teste name atribute"""
        self.assertTrue(hasattr(State, "name"))

    def test_has_attribute(self):
        """Tests if state have the attributes correctly"""
        test_2 = State()
        self.assertTrue(hasattr(test_2, "__init__"))
        self.assertTrue(hasattr(test_2, "created_at"))
        self.assertTrue(hasattr(test_2, "updated_at"))
        self.assertTrue(hasattr(test_2, "id"))

    def test_type(self):
        """tests the type of state attribute for class"""
        self.assertEqual(type(State.name), str)

if __name__ == '__main__':
    unittest.main()
