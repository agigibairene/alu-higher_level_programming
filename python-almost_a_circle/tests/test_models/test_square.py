#!/usr/bin/python3
"""unittest for Rectangle class"""


import unittest
import pep8

from models.square import Square


class Test_a_Square(unittest.TestCase):
    """testing functions for Square class"""

    def test_aaaaa_square_instantiation(self):
        """test initialization of square instance"""
        r3 = Square(24, 45, 16, 73)
        self.assertEqual(r3.id, 73)
        self.assertEqual(r3.width, 24)
        self.assertEqual(r3.height, 24)
        self.assertEqual(r3.x, 45)
        self.assertEqual(r3.y, 16)

    def test_pep8(self):
        """test that code follows pep8 style guidelines"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py',
                                        'models/rectangle.py',
                                        'models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
