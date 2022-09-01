#!/usr/bin/python3
def best_score(a_dictionary):
    """returns a key with the biggest integer value"""
    maxi = 0
    if a_dictionary is None:
        return None
    for i in list(a_dictionary):
        if str(a_dictionary[i]).isdigit() != True:
            return None
        if a_dictionary[i] > maxi:
            maxi = a_dictionary[i]
            k = i
    return k
    """if a_dictionary:
        return max(a_dictionary)"""
