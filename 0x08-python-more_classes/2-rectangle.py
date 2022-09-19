#!/usr/bin/pyton3
"""
Creates a rectangle
Defines aRetangle
"""


class Rectangle:
    """Rectangle defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes a rectangle

        Args:
            width: width of rectangle
            height: of rec
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width

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
        """Retrieves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height

        Args:
            value: of height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area

        Returns:
            Area fo rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Perimeter of rectangle

        Returns:
            Perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
