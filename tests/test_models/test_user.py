#!/usr/bin/python3
"""Test User"""
import unittest
import pep8
from models.user import User


class Testuser(unittest.TestCase):
    """[Test for the class User]
    """

    
    def test_docstring(self):
        """[Checks is docstring exist]
        """
        self.assertTrue(len(User.__doc__) >= 1)
        self.assertTrue(len(User.__init__.__doc__) >= 1)
        self.assertTrue(len(User.__str__.__doc__) >= 1)
        self.assertTrue(len(User.save.__doc__) >= 1)
        self.assertTrue(len(User.to_dict.__doc__) >= 1)
        
    def test_pep8_conformance_user(self):
        """[Test for style of PEP8]
        """
        Style = pep8.StyleGuide(quiet=True)
        result = Style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_User(self):
        """
        [Test attributes to have Class User]
        """
        test_user = User()
        test_user.first_name = 'Betty'
        test_user.last_name = 'Holberton'
        test_user.email = 'user1@holbertonschool.com'
        self.assertEqual(test_user.first_name, 'Betty')
        self.assertEqual(test_user.last_name, 'Holberton')
        self.assertEqual(test_user.email, 'user1@holbertonschool.com')
