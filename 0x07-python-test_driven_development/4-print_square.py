#!/usr/bin/python3
"""
Prints a square with the given size
"""


def print_square(size):
    """Prints a square with the given size.
    parameter
        size: int
            The size is length of the square
    return
        None
    """
    try:
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if size < 0 and isinstance(size, float):
            raise ValueError("size must be must be an integer")

        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
    except Exception as e:
        print(e)
