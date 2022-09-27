#!/usr/bin/python3

"""
JSON representation
"""


def to_json_string(my_obj):
    """
    returns the JSON representation of an
    object'string'
    Args:
        my_obj: the object
    """
    import json
    return json.dumps(my_obj)
