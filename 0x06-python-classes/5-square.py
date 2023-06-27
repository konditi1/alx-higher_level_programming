#!/usr/bin/python3
"""A class that defines a square."""


class Square:
    """Represents a square.

    A square four-sided polygon with equal sides and right angles between them.
    This class provides a basic representation of a square.

    Attributes:
        __size (int): The size (length of the side) of the square.

    Methods:
        __init__(self, size): Constructor for the Square class.
        area(self): Calculates and returns the area of the square.
        my_print(self): Prints the square using the character '#'.
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
        self.__size = size

    @property
    def size(self):
        """Getter method for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for the size attribute.

        Parameters:
            value (int): The new size value to be assigned.

        Raises:
            TypeError: If the value parameter is not an integer.
            ValueError: If the value parameter is less than 0.

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square using the character '#'."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
