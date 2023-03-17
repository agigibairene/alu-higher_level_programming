#!/usr/bin/python3
"""creates a class Square"""


class Square:
    """defines class with private instance
    attributes size and position and public instance methods"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return(self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return(self.__position)

    @position.setter
    def position(self, value):
        check = 0
        while 1:
            if type(value) is not tuple or len(value) is not 2:
                check += 1
                break
            if type(value[0]) is not int or type(value[1]) is not int:
                check += 1
                break
            if value[0] < 0 or value[1] < 0:
                check += 1
            break
        if check is 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return(self.__size * self.__size)

    def my_print(self):
        if self.__size > 0:
            for y in range(self.__position[1]):
                print()
            for column in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for row in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()

    def my_print_string(self):
        square_string = ""
        if self.__size > 0:
            for y in range(self.__position[1]):
                square_string = square_string + "\n"
            for row in range(self.__size):
                for x in range(self.__position[0]):
                    square_string = square_string + " "
                for column in range(self.__size):
                    square_string = square_string + "#"
                if row is not (self.__size - 1):
                    square_string = square_string + "\n"
        return square_string

    def __repr__(self):
        return (self.my_print_string())
