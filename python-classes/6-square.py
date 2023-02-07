#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""create class square"""


class Square:
    """class square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialization of Square object with size.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
    
    @property
    def position(self):
        return self.__position

    

        self.__size = value

    def area(self):

        return (self.__size ** 2)

    def my_print(self):
        if self.__size != 0:
            for i in range(self.__size):
                print("#" * self.__size)
        else:
            print("")
