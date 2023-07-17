#!/usr/bin/python3
"""
Import the Base class and Rectangle class
"""
from models.base import Base
from models.rectangle import Rectangle

"""
Square class that inherits from Rectangle
"""


class Square(Rectangle):
    """
    Square class that inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for the Square class.

        Args:
            size (int): Size of the square.
            x (int): X-coordinate of the square's position. Default is 0.
            y (int): Y-coordinate of the square's position. Default is 0.
            id: ID of the object. Default is None.

        Returns:
            None
        """
        super().__init__(size, size, x, y, id)
        self.width = size
        self.height = size

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"

    @property
    def size(self):
        """
        Getter method for the size attribute.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the square.
        If *args exist and is not empty, **kwargs must be skipped.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            None
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
        Returns the dictionary representation of the square.
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
