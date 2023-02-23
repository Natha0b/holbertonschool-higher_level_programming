#!/usr/bin/python3
"""create class Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """the class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of a square."""
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """The size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
