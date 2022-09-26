#!/usr/bin/python3

"""
creates a class
"""


class BaseGeometry:
    """crreats a class
    def __init__(self, name='', value=0):
        initialies bassegeometry
        Args:
            name: name fo value
            value: int value
        
        self.name = name
        self.value = value
"""
    def area(self):
        """
        area of a geometry
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value

        Args:
            name: the string
            value: the value to be validated
        """
        if type(value) != int:
            e = name + ' must be an integer'
            raise TypeError(e)
        if value <= 0:
            e = name + ' must be greater than 0'
            raise ValueError(e)
