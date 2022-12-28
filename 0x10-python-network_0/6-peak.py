#!/usr/bin/python3
''' contains find_peak function '''


def find_peak(list_of_integers):
    ''' finds a peak in the list '''
    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[len(list_of_integers) - 1]
    return None
