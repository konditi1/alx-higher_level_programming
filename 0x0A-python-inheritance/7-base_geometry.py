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
            raise Exception("area() is not implemented")
        pass
    except Exception as e:
        pass

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
