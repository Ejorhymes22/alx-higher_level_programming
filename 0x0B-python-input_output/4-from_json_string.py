#!/usr/bin/python3

"""
JSON String
"""


def from_json_string(my_str):
    """returns an object
    represented by a json string

    Args:
        my_str: the string
    """
    import json
    return json.loads(my_str)
