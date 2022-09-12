#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """prints the first x elemts of a list andd only integers"""
    j = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end='')
            j += 1
        except (ValueError, TypeError):
            if i == x - 1:
                break
            pass
    print()
    return j
