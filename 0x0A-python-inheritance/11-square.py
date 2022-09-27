#!/usr/bin/python3

"""
clas of square
"""
Rectangle = __import__('9-rectangle').Rectangle



class Square(Rectangle):
    """
    inherits from Rectangle
    """
    def __init__(self, size):
        """initializes a square
        Args:
            size: size fo the squear
        """
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """returns a string"""
        return "[Square] {}/{}".format(self.__size, self.__size)
