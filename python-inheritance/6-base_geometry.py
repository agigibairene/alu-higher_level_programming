#!/usr/bin/python3
"""create a  class BaseGeometry"""


class BaseGeometry:
    """class with public instance method to raise exception"""
    def area(self):
        raise Exception("area() is not implemented")

