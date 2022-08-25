#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    n = 1
    totalsum = 0
    for i in range(n, len(argv)):
        totalsum += int(argv[i])
    print("{}".format(totalsum))
