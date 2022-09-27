#!/usr/bin/python3
"""
lsit of available attributes and methods
of an object
"""


def lookup(obj):
    """returns a list
    of availbale attributes and
    methods of an object

    Args:
        obj: the object
    """
    return list(dir(obj))
