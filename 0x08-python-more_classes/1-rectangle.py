#!/usr/bin/python3
"""
A rectangle class
"""


class Rectangle:
    """A class that defines a rectangle."""

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    """gets the width of the rectangle"""

    @property
    def width(self):
        return self.__width

    """ sets the width of the rectangle"""

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """gets the height of the rectangle"""

    @property
    def height(self):
        return self.__height

    """sets the height of the rectangle"""

    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    """__repr__ method which returns a string representation of the rectangle"""

    def __repr__(self):
        return f"Rectangle(height={self.__height}, width={self.__width})"
