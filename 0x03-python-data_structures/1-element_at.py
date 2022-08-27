#!/usr/bin/python3
def element_at(my_list, idx):
    i = 0
    if idx < 0 or len(my_list) <= idx:
        return None
    return my_list[idx]
