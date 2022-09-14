#!/usr/bin/python3
"""
defines a square
"""


class Square:
    """position and size of a square"""
    def __init__(self, size=0, position=(0, 0)):
        """defines a size and pposition"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """def the size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """gets a position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position to a value."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    """def position(self, value):
        if (not isinstance(value, tuple)) or (type(value[0]) != int) \
                or type(self.value[1]) != int or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
"""
    def area(self):
        """current square area"""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square of xcher #"""
        if self.__size == 0:
            print()
            return
        for z in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end='')
            for k in range(self.__size):
                print("#", end='')
            print()
