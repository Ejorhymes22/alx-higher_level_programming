#!/usr/bin/python3
"""
tests for class
"""


def is_kind_of_class(obj, a_class):
    """
    Returns true or false
    if an instance of the class

    Args:
        obj: the object
        a_class: the class
    """
    return isinstance(obj, a_class)
