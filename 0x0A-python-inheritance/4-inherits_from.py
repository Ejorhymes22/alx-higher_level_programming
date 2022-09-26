#!/usr/bin/python3
"""
tests for class
"""


def inherits_from(obj, a_class):
    """
    Returns true or false
    if an instance of the class

    Args:
        obj: the object
        a_class: the class
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
