#!/usr/bin/python3
"""defines a function that returns the dictionary
description for JSON serialization of an object"""


def class_to_json(obj):
    """returns dictionary description for JSON serialization"""
    return obj.__dict__
