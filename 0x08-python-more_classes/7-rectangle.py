#!/usr/bin/pyton3

"""
creates a rectangle
"""


class Rectangle:
    """
    defines a rectangle
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initializes a rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """dfines the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """defines width"""
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
        """defines hegit"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        s = ''
        if self.width == 0 or self.height == 0:
            return s
        for i in range(self.height):
            for j in range(self.width):
                s += str(self.print_symbol)
            if self.height - 1 > i:
                s += '\n'
        return s
    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """del a rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
