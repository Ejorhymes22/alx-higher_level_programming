#!/usr/bin/python3
"""
This class defines a square
"""


class Square:
    """defines a square with setter"""
    def __init__(self, size=0):
        """size of initial"""
        self.__size = size

    @property
    def size(self):
        """size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """size with correct value"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """arae of the self"""
        return self.__size ** 2
