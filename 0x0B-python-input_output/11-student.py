#!/usr/bin/python3
"""
defines a strudent
"""


class Student:
    """
    class of student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrives a diction repersentation of a student"""
        copy = {}
        if type(attrs) == list:
            for i in attrs:
                for k, j in self.__dict__.items():
                    if i == k:
                        copy[i] = j
            return copy
        return self.__dict__

    def reload_from_json(self, json):
        
        for i, j in json.items():
            for k, l in self.__dict__.items():
                if i == k:
                    self.__dict__[k] = j
        """replaces all attributes of student"""
        """try:
            if (self.json):
                for i in self.__dict__:
                    for k, j in self.json.items():
                        if i == k:
                            self.i = j
        except:
           """ 
