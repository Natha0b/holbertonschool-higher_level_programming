#!/usr/bin/python3
"""create class Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """the class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of a square."""
        
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width)
