#!/usr/bin/python3
"""
Inheritance class
"""


class MyList(list):
    """
    Inherists from list
    """
    def print_sorted(self):
        """
        priints the list but
        sorted

        Args:
            self: the object
        """
        new_list = []
        for i in self:
            new_list.append(i)
        print(sorted(new_list))
