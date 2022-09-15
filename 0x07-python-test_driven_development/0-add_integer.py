#!/usr/bin/python3

"""
This module is
for adding 2 num
if they are int good
if they arefloats change them to int
"""


def add_integer(a, b=98):
    """ Adds two ints together
    Args:
        a: nust be int
        b: must be int
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return a + b
