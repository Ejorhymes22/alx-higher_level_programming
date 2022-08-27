#!/usr/bin/python3
def multiple_returns(sentence):
    """returns a tuple with the lenght of a string and
    its first character"""
    lenght = len(sentence)
    if lenght > 0:
        first = sentence[0]
        return (lenght, first)
    return (lenght, None)
