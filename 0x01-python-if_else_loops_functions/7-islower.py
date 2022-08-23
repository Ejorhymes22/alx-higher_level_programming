#!/usr/bin/python3
def islower(c):
    """checks if a char is lower or upper"""
    for i in range(ord('a'), ord('z')):
        if chr(i) == c:
            return True
    return False
