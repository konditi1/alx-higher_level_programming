#!/usr/bin/env python
"""
base class
"""


class Base:
    """
    base class
    """
    __nb_objects = 0
    """
    a private class attribute __nb_objects for tracking
    the number of objects created
    """
    def __init__(self, id=None):
        """
        constructor for the base class
        :param:
            id: id of the object
        :return:
            nothing
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
