#!/usr/bin/python3
"""
base class
"""
import json
import csv
import turtle

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
        """writes json string repr of list_objs to a file"""
        dict_list = []
        if list_objs is not None:
            for i in list_objs:
                dict_list.append(i.to_dictionary())
        json_string = cls.to_json_string(dict_list)
        with open("().json".format(cls.__name__), "w+", encoding="utf-8") as f:
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
        dummy = cls(1, 1, 2)
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


     @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the Rectangles and Squares"""
        screen_width = 620
        padding = 10
        row_width = padding
        row_height = 0
        screen_height = padding
        color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo',
                      'violet']
        color_size = len(color_list)
        color_index = 0
        for rect in list_rectangles:
            potential_width = row_width + rect.width + rect.x + padding
            if (row_width == padding or potential_width < screen_width):
                row_width += rect.width + rect.x + padding
                if (row_height < rect.height + rect.y):
                    row_height = rect.height + rect.y
            else:
                screen_height += row_height + padding
                row_width = rect.width + rect.x + padding * 2
                row_height = rect.height + rect.y

        for square in list_squares:
            potential_width = row_width + square.size + square.x + padding
            if (row_width == padding or potential_width < screen_width):
                row_width += square.size + square.x + padding
                if (row_height < square.size + square.y):
                    row_height = square.size + square.y
            else:
                screen_height += row_height + padding
                row_width = square.size + square.x + padding * 2
                row_height = square.size + square.y
        turtle.screensize(canvwidth=screen_width, canvheight=screen_height)
        turtle.pu()
        turtle.left(180)
        turtle.forward(screen_width/2 - padding)
        turtle.right(90)
        turtle.forward(screen_height/2 - padding)
        turtle.right(90)
        row_width = padding
        row_height = 0
        for rect in list_rectangles:
            potential_width = row_width + rect.width + rect.x + padding
            if (row_width == padding or potential_width < screen_width):
                row_width += rect.width + rect.x + padding
                if (row_height < rect.height + rect.y):
                    row_height = rect.height + rect.y
            else:
                turtle.pu()
                turtle.left(180)
                turtle.forward(row_width - padding)
                turtle.left(90)
                turtle.forward(row_height + padding)
                turtle.left(90)
                row_width = rect.width + rect.x + padding * 2
                row_height = rect.height + rect.y
            turtle.pd()
            turtle.pencolor(color_list[color_index % color_size])
            for _ in range(4):
                turtle.forward(5)
                turtle.back(5)
                turtle.right(90)
            turtle.pu()
            turtle.forward(rect.x)
            turtle.right(90)
            turtle.forward(rect.y)
            turtle.left(90)
            turtle.pd()
            turtle.pencolor('black')
            turtle.fillcolor(color_list[color_index % color_size])
            turtle.begin_fill()
            for _ in range(2):
                turtle.forward(rect.width)
                turtle.right(90)
                turtle.forward(rect.height)
                turtle.right(90)
            turtle.end_fill()
            color_index += 1
            turtle.pu()
            turtle.forward(rect.width + padding)
            turtle.left(90)
            turtle.forward(rect.y)
            turtle.right(90)

        for square in list_squares:
            potential_width = row_width + square.size + square.x + padding
            if (row_width == padding or potential_width < screen_width):
                row_width += square.size + square.x + padding
                if (row_height < square.size):
                    row_height = square.size + square.y
            else:
                turtle.pu()
                turtle.left(180)
                turtle.forward(row_width - padding)
                turtle.left(90)
                turtle.forward(row_height + padding)
                turtle.left(90)
                row_width = square.size + square.x + padding * 2
                row_height = square.size + square.y
            turtle.pd()
            turtle.pencolor(color_list[color_index % color_size])
            for _ in range(4):
                turtle.forward(5)
                turtle.back(5)
                turtle.right(90)
            turtle.pu()
            turtle.forward(square.x)
            turtle.right(90)
            turtle.forward(square.y)
            turtle.left(90)
            turtle.pd()
            turtle.pencolor('black')
            turtle.fillcolor(color_list[color_index % color_size])
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.right(90)
            turtle.end_fill()
            color_index += 1
            turtle.pu()
            turtle.forward(square.size + padding)
            turtle.left(90)
            turtle.forward(square.y)
            turtle.right(90)

        turtle.getscreen()._root.mainloop()
