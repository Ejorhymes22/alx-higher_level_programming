#!/usr/bin/python3
"""
tests for class
"""


def is_same_class(obj, a_class):
    """
    Returns true or false
    if an instance of the class

    Args:
        obj: the object
        a_class: the class
    """
    if type(obj) is a_class:
        return True
    return False
