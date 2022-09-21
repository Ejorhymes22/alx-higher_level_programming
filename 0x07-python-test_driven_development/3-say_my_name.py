#!/usr/bin/python3

"""
This tests and prints firstand last names
"""


def say_my_name(first_name, last_name=""):
    """
    prints the first and last names
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
