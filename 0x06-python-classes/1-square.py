#!/usr/bin/python3
""" this module is of a square with a private
__size(int) as attribute
"""


class Square:
    """
    Represents a square.

    This class provides a basic representation of a square.

    Attributes:
        __size (int): The size (length of the side) of the square.

    Methods:
        __init__(): Constructor for the Square class.
    """

    def __init__(self, size):
        """
        Constructor for Square class.

        Initializes a new instance of the Square class.

        Parameters:
            size (int): The size (length of the side) of the square.

        Returns:
            None
        """
        self.__size = size
