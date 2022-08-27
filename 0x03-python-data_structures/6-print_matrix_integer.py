#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """prints a matrix of integer"""
    if matrix is None:
        return 0
    for i in matrix:
        for x in i:
            print("{:d}".format(x), end='')
        print()
