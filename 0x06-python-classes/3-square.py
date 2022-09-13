#!/usr/bin/python3

"""
This module introduces area of a square
"""


class Square:
    """class of a square with area"""

    def __init__(self, size=0):
        """initializes the square object with
        size

        Args:
            size: size of the square
        """
        try:
            if size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            print("size must be an integer")
        self.__size = size

    def area(self):
        """area of the square is returned"""
        return self.__size * self.__size
