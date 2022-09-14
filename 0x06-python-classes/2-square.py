#!/usr/bin/python3

"""
This module deals with asquare size
if it is legit
"""


class Square:
    """defines a square"""
    def __init__(self, size=0):
        """defines the size of a squase
        as private instance attribute

        Args:
        size: Describes the size of a square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
