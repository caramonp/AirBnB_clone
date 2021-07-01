#!/usr/bin/python3
"""[Test for the console]
"""
import unittest
import pep8


class Testconsole(unittest.TestCase):
    """[class for testing the console]
    """

    # def test_pep8_console(self):
    #     """[Test for style of PEP8]
    #     """
    #     Style = pep8.StyleGuide(quiet=True)
    #     result = Style.check_files(['console.py'])
    #     self.assertEqual(result.total_errors, 0,
    #                      "Found code style errors (and warnings).")

if __name__ == '__main__':
    unittest.main()
