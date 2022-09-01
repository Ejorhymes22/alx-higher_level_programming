#!/usr/bin/python3
def roman_to_int(roman_string):
    """converts a roman numeral to an integer"""
    a_dict = dict(X=10, V=5, I=1, L=50, C=100, D=500, M=1000)
    sums = 0
    s = roman_string
    if s is None or type(s) != str:
        return 0

    for i in range(0, len(roman_string)):
        if s[i] not in a_dict:
            return 0
        elif i > 0:
            if a_dict[s[i - 1]] >= a_dict[s[i]]:
                if i + 1 < len(s):
                    if s[i + 1] not in a_dict:
                        return 0
                    if a_dict[s[i + 1]] <= a_dict[s[i]]:
                        sums += a_dict[s[i]]
                    else:
                        sums -= a_dict[s[i]]
                else:
                    sums += a_dict[s[i]]

            elif i < 2 and a_dict[s[i - 1]] <= a_dict[s[i]]:
                sums -= a_dict[s[i]]
            else:
                sums += a_dict[s[i]]
        else:
            sums += a_dict[s[i]]
    if sums < 0:
        sums = -sums
    return sums
