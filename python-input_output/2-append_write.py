#!/usr/bin/python3
"""defines a function that appends string to text file
and returns the number of characters added"""


def append_write(filename="", text=""):
    """appends string to text file"""
    with open(filename, 'a') as f:
        return f.write(text)
