#!/usr/bin/python3
"""
class called BaseGeometry
"""


class BaseGeometry:
    """
    class called BaseGeometry
    """
    try:
        def area(self):
            """area() is not implemented"""
            raise Exception("area() is not implemented")

    except Exception as e:
        pass

    def integer_validator(self, name, value):
        """integer_validator() is not implemented"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    class called Rectangle
    attributes:
        width: integer
        height: integer
    methods:
        __init__(self, width, height)
        area(self)
        integer_validator(self, name, value)
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """:returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """:returns a string representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """
    class called Square
    attributes:
        size: integer
    methods:
        __init__(self, size)
        area(self)
        integer_validator(self, name, value)
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """:returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """:returns a string representation of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
