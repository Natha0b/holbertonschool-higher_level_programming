#!/usr/bin/python3
'''Write a class Student'''


class Student():
    '''Defines a student'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        if attrs is None:
            return self.__dict__

        dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                dict[attr] = getattr(self, attr)
        return dict

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
