#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """deletes keys with a specific value in a dictionary"""
    for i, k in a_dictionary.items():
        if k == value:
            x = i
    if x in a_dictionary:
        del a_dictionary[x]
    return a_dictionary
