#!/usr/bin/python3
"""A class that defines a square."""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Constructor for the Square class.

        Parameters:
        - size: int, optional
            The size of the square. Defaults to 0.
        - position: tuple, optional
            The position of the square. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method for the size attribute."""
        return self._size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Parameters:
        - value: int
            The size of the square.

        Raises:
        - TypeError: If the value is not an integer.
        - ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        """Getter method for the position attribute."""
        return self._position

    @position.setter
    def position(self, value):
        """
        Setter method for the position attribute.

        Parameters:
        - value: tuple
            The position of the square.

        Raises:
        - TypeError: If the value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = value
        if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
        - int: The area of the square.
        """
        return self.size ** 2

    def my_print(self):
        """Prints the square with the character '#'."""
        if self.size == 0:
            print()
            return

        x, y = self.position
        for _ in range(y):
            print()

        for _ in range(self.size):
            print(" " * x + "#" * self.size)

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
        - str: A string representing the square.
        """
        if self.size == 0:
            return ""

        x, y = self.position
        result = ""
        for _ in range(y):
            result += "\n"

        for _ in range(self.size):
            result += "_" * x + "#" * self.size + "\n"

        return result.rstrip()
