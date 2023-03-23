#!/usr/bin/python3
"""a function that checks if an object is an instance of,
or if the object is an instance of a class that inherited
from the class"""


def is_kind_of_class(obj, a_class):
    """returns True if object is an instance of the class
    or class that inherited from"""
    return (isinstance(obj, a_class))
