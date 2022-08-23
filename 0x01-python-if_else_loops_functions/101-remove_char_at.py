#!/usr/bin/python3
def remove_char_at(str, n):
    """creates a copy of str withont the char at n"""
    x = ''
    k = 0
    for i in str:
        k += 1
        if k == n + 1:
            pass
        else:
            x += i
    return x
