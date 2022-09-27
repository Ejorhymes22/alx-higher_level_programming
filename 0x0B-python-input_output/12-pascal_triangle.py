#!/usr/bin/python3
"""
pascal triangle repr
"""


def pascal_triangle(n):
    """
    returns a list of list
    of integers repr
    pascal triange
    Args:
        n: the int
    """
    p, i, j, past, outer = 1, 0, 1, [1], [[1]]

    if n <= 0:
        return []
    while j < n:
        inner_list = []
        while i < p:
            if i == 0:
                inner_list.append(past[i])
            if i < len(past) - 1:
                inner_list.append(past[i] + past[i + 1])
            if i == len(past) - 1:
                inner_list.append(past[i])
            i += 1
        past = inner_list
        outer.append(inner_list)
        i = 0
        p = p + 1
        j += 1
    return outer
