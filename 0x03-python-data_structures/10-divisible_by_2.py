#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """finds all multiples of a 2 in a list"""
    if len(my_list) == 0:
        return None
    x = []
    for i in my_list:
        if i % 2 == 0:
            x.append(True)
        else:
            x.append(False)
    return x
