#!/usr/bin/python3
"""defines a function that writes an object to a text file
using JSON representation"""


def save_to_json_file(my_obj, filename):
    """write JSON representation of an object to a file"""
    import json
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj, ensure_ascii=False))
