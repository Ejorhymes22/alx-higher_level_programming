#!/usr/bin/python3
"""
search and inserts a newline
"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each
    line containing a specific string
    Args:
        filename: the file
        search_string: the string to searchfor
        new_string: to insert
    """
    with open(filename, "r", encoding='utf-8') as f:
        list_contents = list(f)
    i = 0
    for line in list_contents:
        i += 1
        if search_string in line:
            list_contents.insert(i, new_string)
    with open(filename, "w") as f:
        list_contents = "".join(list_contents)
        f.write(list_contents)
