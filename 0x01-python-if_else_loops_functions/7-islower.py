#!/usr/bin/python3
def islower(c):
    """checks if a char is lower"""
    if ord(c) < ord('a') or ord(c) > ord('z'):
        return False
    return True
