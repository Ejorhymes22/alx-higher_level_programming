#!/usr/bin/python3
"""
prints a square with the character#
"""


def print_square(size):
    """
    square with the character #
    equal to the size
    """
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
