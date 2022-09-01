#!/usr/bin/python3
def best_score(a_dictionary):
    """returns a key with the biggest integer value"""
    maxi = 0
    if not a_dictionary:
        return None
    for i in list(a_dictionary):
        if type(a_dictionary[i]) is not int:
            return None
        if a_dictionary[i] > maxi:
            maxi = a_dictionary[i]
            k = i
    return k
    """if a_dictionary:
        return max(a_dictionary)"""
