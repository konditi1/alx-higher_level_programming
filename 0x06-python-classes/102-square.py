#!/usr/bin/python3
"""A class that defines a square."""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0):
        """
        Constructor for the Square class.

        Parameters:
        - size: int or float, optional
            The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Getter method for the size attribute."""
        return self._size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Parameters:
        - value: int or float
            The size of the square.

        Raises:
        - TypeError: If the value is not a number (int or float).
        - ValueError: If the value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
        - int or float: The area of the square.
        """
        return self.size ** 2

    def __eq__(self, other):
        """
        Equality comparator for squares based on their area.

        Parameters:
        - other: Square
            The other square to compare.

        Returns:
        - bool: True if the areas are equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return NotImplemented

    def __ne__(self, other):
        """
        Inequality comparator for squares based on their area.

        Parameters:
        - other: Square
            The other square to compare.

        Returns:
        - bool: True if the areas are not equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() != other.area()
        return NotImplemented

    def __gt__(self, other):
        """
        Greater than comparator for squares based on their area.

        Parameters:
        - other: Square
            The other square to compare.

        Returns:
        - bool: True if the area is greater, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """
        Greater than or equal comparator for squares based on their area.

        Parameters:
        - other: Square
            The other square to compare.

        Returns:
        - bool: True if the area is greater or equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented

    def __lt__(self, other):
        """
        Less than comparator for squares based on their area.

        Parameters:
        - other: Square
            The other square to compare.

        Returns:
        - bool: True if the area is less, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """
        Less than or equal comparator for squares based on their area.

        Parameters:
        - other: Square
            The other square to compare.

        Returns:
        - bool: True if the area is less or equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented
