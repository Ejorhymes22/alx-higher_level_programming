#!/usr/bin/python3
"""
inherits from int
"""


class MyInt(int):
    """
    myint is a rebel
    it inherits from int
    but has == and != mixed
    """
    def __init__(self, value):
        """initializes the value"""
        self.__value = value

    def __str__(self):
        return "{}".format(self.__value)

    def __eq__(self, other):
        return self.__value != other

    def __ne__(self, other):
        return self.__value == other
