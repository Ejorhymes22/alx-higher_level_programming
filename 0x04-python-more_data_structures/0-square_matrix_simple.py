#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """computes the square vallue of all integers of a matrix
    x = []
    k = 0
    for i in matrix:
        x.append([])
        for z in i:
            x[k].append(z ** 2)
        k += 1
    return x"""
    x = []
    for i in matrix:
        x.append(list(map(lambda x: x ** 2, i)))
    return x
