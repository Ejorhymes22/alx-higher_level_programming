#!/usr/bin/python3
""" this class defines a square
"""


class Square:
    """defines and prints a square"""
    def __init__(self, size=0):
        """initialisees the square"""
        self.__size = size

    @property
    def size(self):
        """the size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """checking value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """gets the area of squaer"""
        return self.__size * 2

    def my_print(self):
        """prints in stdout the square with the xter #"""
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print()
        if self.__size == 0:
            print("")
