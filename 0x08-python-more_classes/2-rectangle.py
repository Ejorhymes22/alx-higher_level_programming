#!/usr/bin/pyton3

"""
creates a rectangle
"""


class Rectangle:
    """defines a rectangle"""

    def __init__(self, width=0, height=0):
        """initializes a rectangle

        Args:
            width: width of rectangle
            height: of rec
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """dfines the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """defines width

        Args:
            value: value fo width
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
            value: of height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)
