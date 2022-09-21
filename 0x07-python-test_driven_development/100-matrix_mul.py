#!/usr/bin/python3
"""
Multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """
    function multiplies 2 matrices
    """
    k, l, m = 0, 0, 0
    x = []
    y = []

    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")
    for i in m_a:
        if type(i) != list:
            raise TypeError("m_a must be a list of lists")
    for i in m_b:
        if type(i) != list:
            raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for i in m_a:
        l = 0
        for j in i:
            l += 1
            if type(j) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
        x.append(l)

    for i in m_b:
        m = 0
        for j in i:
            m += 1
            if type(j) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
        y.append(m)

    if len(set(x)) != 1:
        raise TypeError("each row of m_a must be of the same size")
    if len(set(y)) != 1:
        raise TypeError("each row of m_b must be of the same size")

    for i in m_b:
        k += 1
    if len(m_a[0]) != k:
        raise ValueError("m_a and m_b can't be multiplied")

    rez = [[m_b[j][i] for j in range(len(m_b))] for i in range(len(m_b[0]))]
    b = []

    for i in m_a:
        a = []
        for j in rez:
            z = 0
            k = 0
            while(k < len(i)):
                z += i[k] * j[k]
                k += 1
            a.append(z)
        b.append(a)
    return b
