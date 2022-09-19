#!/usr/bin/pyton3

"""
creates a rectangle
"""


class Rectangle:
    """
    defines a rectangle
    """
    @property
    def width(self):
        """dfines the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """defines width

        Args:
            value: value of width positive int
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """dfines the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """defines hegit

        Args:
            value: must be width positive int
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __init__(self, width=0, height=0):
        """initializes a rectangle

        Args:
            width: must be an int
            height: of the rectangle
        """
        self.width = width
        self.height = height
