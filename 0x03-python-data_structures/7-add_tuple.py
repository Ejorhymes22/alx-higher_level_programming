#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """adds two tuples together"""
    i = 0
    x = list(tuple_a)
    y = list(tuple_b)
    tople = []

    while i < 2:
        if len(x) < 2:
            x.append(0)
        if len(y) < 2:
            y.append(0)
        tople.append(x[i] + y[i])
        i += 1
    return tuple(tople)
