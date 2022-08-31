#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """replaces all occurences of a n element by another in a new list"""
    x = list(map(lambda x: replace if x == search else x, my_list))
    return x
