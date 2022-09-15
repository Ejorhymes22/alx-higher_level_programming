#!/usr/bin/python3
"""
This tests andd dividess a matrix
by varoius stancards
"""


def matrix_divided(matrix, div):
    """
    divides ll elements of a matrix
    """
    if type(matrix) != list or type(matrix[0]) != list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    x = len(matrix[0])
    z = []
    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    for i in matrix:
        if type(i) != list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if x != len(i):
            raise TypeError("Each row of the matrix must have the same size")
        y = []
        for j in range(len(matrix[0])):
            y.append(round((i[j] / div), 2))
        z.append(y)
    return z
