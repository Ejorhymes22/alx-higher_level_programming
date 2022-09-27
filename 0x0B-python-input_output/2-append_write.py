#!/usr/bin/python3

"""
appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """returns the number of characters
    Args:
        filename: the file
        text: the text
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
