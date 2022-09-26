#!/usr/bin/python3
"""
About Inheritance
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Inherits from baseclas"""
    def __init__(self, width, height):
        """initialies rectangele

        Args:
            width: with of rectange
            height: its height
        """
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
