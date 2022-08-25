#!/usr/bin/python3

import hidden_4
if __name__ == "__main__":
    """
    i = 0
    arr = dir(hidden_4)
    while (len(arr) > i):
        if arr[i][0] != '_':
            print("{}".format(arr[i]))
        i += 1"""
    for element in dir(hidden_4):
        if element[0] != "_":
            print(element)
