#!/usr/bin/python3
"""
dictionary representation
of an obj
"""


def class_to_json(obj):
    """return a dict description with
    simple data structure
    for JSON serializetion of obj
    Args:
        obj: the obj
    """
    return obj.__dict__
