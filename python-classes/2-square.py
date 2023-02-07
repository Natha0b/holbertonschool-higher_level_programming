#!/usr/bin/python3
"""create class square"""


class Square:
    """class square"""
    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
