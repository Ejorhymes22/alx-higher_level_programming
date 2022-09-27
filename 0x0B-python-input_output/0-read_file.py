#!/usr/bin/python3

"""
This reads a text file
"""


def read_file(filename=""):
    """function theat reads
    a text file
    Args:
        filename: the file name
    """
    with open(filename, encoding="utf-8") as f:
        q = f.read()
        print("{}".format(q), end='')
