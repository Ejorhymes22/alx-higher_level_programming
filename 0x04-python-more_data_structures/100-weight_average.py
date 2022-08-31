#!/usr/bin/python3
def weight_average(my_list=[]):
    """returns the weighted average of all integers tuple"""
    sums, sumW, mul = 0, 0, 1
    if my_list == [] or my_list == None:
        return 0
    for i in my_list:
        for x in range(0, 2):
            if x == 1:
                sumW += i[x]
            mul *= i[x]
        sums += mul
        mul = 1
    return sums / sumW
