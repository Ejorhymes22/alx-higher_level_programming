#!/usr/bin/python3
def uniq_add(my_list=[]):
    """adds all  unique integers in a list"""
    x = set(my_list)
    sum = 0
    for i in x:
        sum += i
    return sum
