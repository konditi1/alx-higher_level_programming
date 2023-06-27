#!/usr/bin/python3
"""A class that defines a square."""


class Square:
    """Represents a square.

    A square four-sided polygon with equal sides and right angles between them.
    This class provides a basic representation of a square.

    Attributes:
        __size (int): The size (length of the side) of the square.
        __position (tuple): The position of the square.

    Methods:
        __init__(self, size, position): Constructor for the Square class.
        size(self): Getter method for the size attribute.
        size(self, value): Setter method for the size attribute.
        position(self): Getter method for the position attribute.
        position(self, value): Setter method for the position attribute.
        area(self): Calculates and returns the area of the square.
        my_print(self): Prints the square using the character '#'.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Constructor for the Square class.

        Initializes new instance of Square class with a given size and position.

        Parameters:
            size (int): The size (length of the side) of the square. Default is 0.
            position (tuple): The position of the square. Default is (0, 0).

        Raises:
            TypeError: If the size parameter is not an integer or
            if the position parameter is not a tuple of 2 positive integers.
            ValueError: If the size parameter is less than 0 or if the
            position parameter contains invalid values.

        Returns:
            None
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter method for the position attribute.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for the position attribute.

        Parameters:
            value (tuple): The new position value to be assigned.

        Raises:
            TypeError: If value parameter is not tuple of 2 positive integers.
            ValueError: If the value parameter contains invalid values.

        Returns:
            None
        """
        if not isinstance(value, tuple) or len(value) != 2 or not\
                        all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square using the character '#' and position attribute."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
