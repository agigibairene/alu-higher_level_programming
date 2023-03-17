#!/usr/bin/python3
"""creates a class Rectangle"""


class Rectangle:
    """defines class Rectangle with
private instance attributes and 
public instance methods"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return ((2 * self.width) + (2 * self.height))

    def __str__(self):
        rec_string = ""
        if self.width == 0 or self.height == 0:
            return (rec_string)
        for row in range(self.height):
            for column in range(self.width):
                rec_string += "#"
            rec_string += "\n"
        rec_string = rec_string[:-1]
        return (rec_string)
