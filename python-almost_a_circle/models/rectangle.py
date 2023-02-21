#!/usr/bin/python3
"""create class Rectangle"""
from models.base import Base


class Rectangle:
    """the class Rectangle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
