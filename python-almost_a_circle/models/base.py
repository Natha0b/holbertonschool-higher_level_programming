#!/usr/bin/python3
"""the first class Base"""
import json
import os.path


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """that returns the JSON string representation
        of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """that writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        list_n = []
        with open(f"{cls.__name__}.json", "w") as file:
            for i in list_objs:
                list_n.append(i.to_dictionary())
            list_n = cls.to_json_string(list_n)
            file.write(list_n)

    @staticmethod
    def from_json_string(json_string):
        """that returns the list of the JSON string representation"""
        list = []
        if json_string is None or len(json_string) == 0:
            return list
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ that returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1)

        if cls.__name__ == "Square":
            instance = cls(1)

        instance.update(**dictionary)

        return instance

    @classmethod
    def load_from_file(cls):
        """that returns a list of instances"""
        ret = []
        filename = "{}.json".format(cls.__name__)
        if os.path.isfile(filename):
            with open(filename, "r") as file:
                str_list = file.read()
            dict_list = cls.from_json_string(str_list)
            for obj_dict in dict_list:
                new = cls.create(**obj_dict)
                ret.append(new)
            return ret
