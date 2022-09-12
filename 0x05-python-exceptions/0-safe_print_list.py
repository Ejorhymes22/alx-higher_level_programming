#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """prints c elements of a list"""
    try:
        for i in range(0, x):
            print("{}".format(my_list[i]), end='')
        print()
    except IndexError:
        print()
        return i
    else:
        return x
