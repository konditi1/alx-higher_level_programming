# !/usr/bin/python3
"""
import the Base class and Rectangle class
"""
from models.base import Base
from models.rectangle import Rectangle

"""
square class that inherits from Rectangle
"""


class Square(Rectangle):
    """
    square class that inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        constructor for the square class
        param:
            size: size of the square
            x: x-coordinate of the square
            y: y-coordinate of the square
            id: id of the object
        return:
            nothing
        """
        super().__init__(size, size, x, y, id)
        self.width = size
        self.height = size

    def __str__(self):
        """
        returns a string representation of the square
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"

    @property
    def size(self):
        """
        getter method for the size attribute
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter method for the size attribute
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        updates the attributes of the square
        if *args exist and is not empty: **kwargs must be skipped
        """
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        if len(args) > 1:
            self.id = args[0]
        if len(args) > 2:
            self.size = args[1]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]

    def to_dictionary(self):
        """
        returns the dictionary representation of the square
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
