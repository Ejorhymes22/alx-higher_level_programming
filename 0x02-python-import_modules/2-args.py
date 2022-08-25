#!/usr/bin/python3
import sys
if __name__ == "__main__":
    count = len(sys.argv)
    count = count - 1
    n = 0

    if count == 1:
        print("1 argument:")
    elif count == 0:
        print("0 arguments.")
    else:
        print(f"{count} arguments:")
    while count > n:
        print("{}: {}".format((n + 1), sys.argv[n + 1]))
        n += 1
