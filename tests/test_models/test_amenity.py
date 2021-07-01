#!/usr/bin/python3
"""
[Unittest for Test amenity]
"""
from models.amenity import Amenity
import unittest
# import pep8


class TestAmenity(unittest.TestCase):
    """Test for the class Amenity"""

    def test_docstring(self):
        """[Checks is docstring exist]
        """
        self.assertTrue(len(Amenity.__doc__) > 1)
        self.assertTrue(len(Amenity.__init__.__doc__) > 1)
        self.assertTrue(len(Amenity.__str__.__doc__) > 1)
        self.assertTrue(len(Amenity.save.__doc__) > 1)
        self.assertTrue(len(Amenity.to_dict.__doc__) > 1)

    # def test_pep8(self):
    #     """[Test for pep8]
    #     """
    #     style = pep8.StyleGuide(quiet=True)
    #     result = style.check_files(['models/amenity.py'])
    #     self.assertEqual(result.total_errors, 0, "fix pep8")

    def test_has_attribute(self):
        """[Tests if Amenety have the attributes correctly]
        """
        test_2 = Amenity()
        self.assertTrue(hasattr(test_2, "__init__"))
        self.assertTrue(hasattr(test_2, "created_at"))
        self.assertTrue(hasattr(test_2, "updated_at"))
        self.assertTrue(hasattr(test_2, "id"))

    def test_name_amenity(self):
        """[Test attribute name of Class Amenity]
        """
        my_amenity = Amenity()
        my_amenity.name = "Wi-Fi"
        self.assertEqual(my_amenity.name, 'Wi-Fi')

if __name__ == '__main__':
    unittest.main()
