#!/usr/bin/python3
def uppercase(str):
    """turns a string to uppercase"""
    x = ""
    y = 0
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            y = ord(i) - 32
            x += chr(y)
        else:
            x += i
    print("{}".format(x))
