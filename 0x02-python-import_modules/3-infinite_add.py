#!/usr/bin/python3

if __name__ == "main":
    from sys import argv
    n = 1
    totalsum = 0
    for i in range(n, len(argv)):
        totalsum += int(argv[i])
    print("{}".format(totalsum))
