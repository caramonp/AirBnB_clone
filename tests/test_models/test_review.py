#!/usr/bin/python3
""" test Review """

import unittest
import models
import os
from models.review import Review


class TestPlace(unittest.TestCase):
    """ Test class Review"""

    def test_pep8(self):
        """ test pep8 style"""
        self.assertEqual(os.system('pep8 models/review.py'), 0)

    def test_module_docstring(self):
        """test documentation"""
        self.assertTrue(len(Review.__doc__) >= 1)
        self.assertTrue(len(Review.__init__.__doc__) >= 1)

    def test_name_file(self):
        """teste name atribute"""
        self.assertTrue(hasattr(Review, "place_id"))
        self.assertTrue(hasattr(Review, "user_id"))
        self.assertTrue(hasattr(Review, "text"))

    def test_has_attribute(self):
        """Tests if Review have the attributes correctly"""
        test_2 = Review()
        self.assertTrue(hasattr(test_2, "__init__"))
        self.assertTrue(hasattr(test_2, "created_at"))
        self.assertTrue(hasattr(test_2, "updated_at"))
        self.assertTrue(hasattr(test_2, "id"))

    def test_type(self):
        """tests the type of Review attribute for class"""
        self.assertEqual(type(Review.place_id), str)
        self.assertEqual(type(Review.user_id), str)
        self.assertEqual(type(Review.text), str)

if __name__ == '__main__':
    unittest.main()
