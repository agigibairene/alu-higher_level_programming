#!/usr/bin/python3
""" class MyList that inherits from list"""


class MyList(list):
     """A class MyList that inherits from list
    with public instance method to print sorted list"""

    def print_sorted(self):
        print(sorted(self))
