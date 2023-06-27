#!/usr/bin/python3
"""A class that defines a square."""


class Square:
    """Represents a square.

    A square four-sided polygon with equal sides, right angles between them.
    This class provides a basic representation of a square.

    Attributes:
        __size (int): The size (length of the side) of the square.

    Methods:
        __init__(self, size): Constructor for the Square class.
    """

    def __init__(self, size=0):
        """Constructor for the Square class.

        Initializes a new instance of the Square class with a given size.

        Parameters:
            size (int): The length of the side of the square. Default is 0.

        Raises:
            TypeError: If the size parameter is not an integer.
            ValueError: If the size parameter is less than 0.

        Returns:
            None
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
