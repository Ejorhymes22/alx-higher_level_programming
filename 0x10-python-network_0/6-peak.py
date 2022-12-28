#!/usr/bin/python3
''' contains find_peak function '''


def find_peak(list_of_integers):
    ''' finds a peak in the list '''
    if list_of_integers:
        li = sorted(list_of_integers)
        return li[len(li) - 1]
    return None
