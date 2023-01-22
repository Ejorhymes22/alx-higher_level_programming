#!/usr/bin/python3

# def complex_delete(a_dictionary, value):
#     """deletes keys with a specific value in a dictionary"""
#     z = 0
#     for i in range(0, len(a_dictionary)):
#         x = None
#         for i, k in a_dictionary.items():
#             if k == value:
#                 x = i
#                 break
#         if x is not None:
#             del a_dictionary[x]
#     return a_dictionary


def complex_delete(a_dictionary, value):
    for key in list(a_dictionary.keys()):
        if a_dictionary[key] == value:
            del a_dictionary[key]
