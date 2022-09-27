#!/usr/bin/python3
"""
obj to text file
"""


def save_to_json_file(my_obj, filename):
    """
    writes an obj to a text file
    using a JSON representation
    Args:
        my_obj: the object
        filename: file
    """
    import json

    with open(filename, "w+", encoding='utf-8') as f:
        json.dump(my_obj, f)
