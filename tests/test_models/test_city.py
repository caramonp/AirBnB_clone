#!/usr/bin/python3
"""[Test City]
"""
from models.city import City
import pep8
import unittest


class Testcity(unittest.TestCase):
    """[Test for the class City]
    """

    def test_docstring(self):
        """[Checks is docstring exist]
        """
        self.assertTrue(len(City.__doc__) >= 1)
        self.assertTrue(len(City.__init__.__doc__) >= 1)
        self.assertTrue(len(City.__str__.__doc__) >= 1)
        self.assertTrue(len(City.save.__doc__) >= 1)
        self.assertTrue(len(City.to_dict.__doc__) >= 1)

    # def test_pep8_conformance_city(self):
    #     """[Test that for style PEP8]
    #     """
    #     Style = pep8.StyleGuide(quiet=True)
    #     result = Style.check_files(['models/city.py'])
    #     self.assertEqual(result.total_errors, 0,
    #                      "Found code style errors (and warnings).")

    def test_class(self):
        """[Test if the name class es City]
        """
        city1 = City()
        self.assertEqual(city1.__class__.__name__, "City")

    def test_city(self):
        """
        Test attributes of Class City
        """
        my_city = City()
        my_city.name = "Medellin"
        self.assertEqual(my_city.name, 'Medellin')

    def test_after_to_dict(self):
        """[Test if City have the attributes correctl]
        """
        my_model = City()
        new_model = City()
        test_dict = my_model.to_dict()
        self.assertIsInstance(my_model, City)
        self.assertEqual(type(my_model).__name__, "City")
        self.assertEqual(test_dict['__class__'], "City")
        self.assertTrue(type(test_dict['__class__']), 'str')
        self.assertTrue(type(test_dict['created_at']), 'str')
        self.assertTrue(type(test_dict['updated_at']), 'str')
        self.assertTrue(type(test_dict['id']), 'str')
        self.assertNotEqual(my_model.id, new_model.id)

if __name__ == '__main__':
    unittest.main()
