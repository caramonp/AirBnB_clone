#!/usr/bin/python3
""" test place """

import unittest
import models
import os
from models.place import Place


class TestPlace(unittest.TestCase):
    """ Test class Place"""

    def test_pep8(self):
        """ test pep8 style"""
        self.assertEqual(os.system('pep8 models/place.py'), 0)
    
    def test_module_docstring(self):
        """test documentation"""
        self.assertTrue(len(Place.__doc__) >= 1)
        self.assertTrue(len(Place.__init__.__doc__) >= 1)

    def test_name_file(self):
        """teste name atribute"""
        self.assertTrue(hasattr(Place, "city_id"))
        self.assertTrue(hasattr(Place, "user_id"))
        self.assertTrue(hasattr(Place, "name"))
        self.assertTrue(hasattr(Place, "description"))
        self.assertTrue(hasattr(Place, "number_rooms"))
        self.assertTrue(hasattr(Place, "number_bathrooms"))
        self.assertTrue(hasattr(Place, "price_by_night"))
        self.assertTrue(hasattr(Place, "latitude"))
        self.assertTrue(hasattr(Place, "longitude"))
        self.assertTrue(hasattr(Place, "amenity_ids"))

    def test_has_attribute(self):
        """Tests if place have the attributes correctly"""
        test_2 = Place()
        self.assertTrue(hasattr(test_2, "__init__"))
        self.assertTrue(hasattr(test_2, "created_at"))
        self.assertTrue(hasattr(test_2, "updated_at"))
        self.assertTrue(hasattr(test_2, "id"))

    def test_type(self):
        """tests the type of place attribute for class"""
        self.assertEqual(type(Place.city_id), str)
        self.assertEqual(type(Place.user_id), str)
        self.assertEqual(type(Place.name), str)
        self.assertEqual(type(Place.description), str)
        self.assertEqual(type(Place.number_rooms), int)
        self.assertEqual(type(Place.number_bathrooms), int)
        self.assertEqual(type(Place.max_guest), int)
        self.assertEqual(type(Place.price_by_night), int)
        self.assertEqual(type(Place.latitude), float)
        self.assertEqual(type(Place.longitude), float)
        self.assertEqual(type(Place.amenity_ids), list)

if __name__ == '__main__':
    unittest.main()
