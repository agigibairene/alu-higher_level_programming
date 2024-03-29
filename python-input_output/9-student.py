#!/usr/bin/python3
"""defines a class Student that defines a
student by public instance attributes"""


class Student():
    """class to define student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
