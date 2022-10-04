#!/usr/bin/python3
"""
base class
"""


import json
import csv


class Base:
    """this is the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constuctor"""
        if id is None:
            Base.__nb_objects += 1
            id = Base.__nb_objects
        self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the json repr. of a string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes json string repr of
        list_objs to a file
        """
        dict_list = []
        if list_objs is not None:
            for i in list_objs:
                dict_list.append(i.to_dictionary())
        json_string = cls.to_json_string(dict_list)
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the json string repr"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1, 2)
        elif cls.__name__ == "Square":
            dummy = cls(1, 1)
        else:
            dummy = None
        cls.update(dummy, **dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        try:
            with open("{}.json".format(cls.__name__), "r") as f:
                s = f.read()
        except FileNotFoundError:
            return []
        list_json = (cls.from_json_string(s))
        create_list = []
        for i in list_json:
            create_list.append(cls.create(**i))
        return create_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save a csv format in a file"""
        dict_list = []
        if list_objs is not None:
            for i in list_objs:
                dict_list.append(i.to_dictionary())
            dict_keys = []
            for i, k in dict_list[0].items():
                dict_keys.append(i)
            with open("{}.csv".format(cls.__name__), "w+") as csvfile:
                for i in range(len(dict_list)):
                    writer = csv.DictWriter(csvfile,
                                            fieldnames=dict_list[i].keys())
                    writer.writeheader()
                    writer.writerows(dict_list)

    @classmethod
    def load_from_file_csv(cls):
        """deserialises a csv"""
        dict_list = []
        try:
            with open("{}.csv".format(cls.__name__), "r") as csv_f:
                for i in (csv.reader(csv_f)):
                    dict_list.append(i)
                    print(i)
        except FileNotFoundError:
            return []
        create_list = []
        for i in dict_list:
            create_list.append(cls.create(**i))
        return create_list
