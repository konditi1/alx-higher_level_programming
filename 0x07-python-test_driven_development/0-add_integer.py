#!/usr/bin/python3
"""
module which adds two integers
"""


def add_integer(a, b=98):
    """
    add_integer - function which performs addition of
                  two integers or floats
    Parameters:
        a: first integer or float
        b: second integer or float
    Returns:
        Sum of two integers or floats
    """
    try:
        if not isinstance(a, (int, float)):
            raise TypeError("a must be an integer")
        if not isinstance(b, (int, float)):
            raise TypeError("b must be an integer")
        a = int(a)
        b = int(b)
        return a + b
    except (ValueError, TypeError) as e:
        return (e)
