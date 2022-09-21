#!/usr/bin/python3

"""
This prints a text
"""


def text_indentation(text):
    """prints a text with 2 new lines
    after each of these characters
    ., ?, :
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    j = 0
    #for j in range(len(text)):
    while j < len(text):
        i = j
        if text[j] == '.' or text[j] == '?' or text[j] == ':':
           print(text[j])
           print()
           j += 1
        else:
            k = ''
            #print("{}".format(text[j]), end='')
            while i < len(text):
                if text[i] == '.' or text[i] == '?' or text[i] == ':':
                    break
                k += text[i]
                i += 1
            j = i
            print("{}".format(k.strip()), end='')
