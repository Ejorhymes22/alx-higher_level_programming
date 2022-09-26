#!/usr/bin/python3

"""
adds a new attribute if possibe
"""


def add_attribute(obj, name, value):
    """
    adds a new attribute to an ognect
    """
#    print(dir(obj))
    if "__dict__" in dir(obj):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
