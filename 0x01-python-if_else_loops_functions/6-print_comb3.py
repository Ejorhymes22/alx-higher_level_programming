#!/usr/bin/python3
for i in range(0, 9):
    for k in range(i + 1, 10):
        if i != 8 or k != 9:
            print("{}{}, ".format(i, k), end="")
print("{}{}".format(i, k))
