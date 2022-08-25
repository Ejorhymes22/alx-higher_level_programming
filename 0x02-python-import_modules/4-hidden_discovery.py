#!/usr/bin/python3

import hidden_4
if __name__ == "__main__":
    i = 0
    arr = dir(hidden_4)
    while (len(arr) > i):
        print("{}".format(arr[i]))
        i += 1
