#!/usr/bin/python3
"""creates a class with private instance attribute size"""

class Square:
    """defines class with a private intance attribut size and zise must be integer otherwise raise a TypeError"""
     def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
