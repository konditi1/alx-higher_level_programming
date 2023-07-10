#!/usr/bin/python3
"""
function which returns True if the object is an instance of, or
if the object is an instance of a class that inherited from,
the specified class else False
"""


def is_kind_of_class(obj, a_class):
    """
    function which returns True if the object is an instance of a
    class else False
    parameter:
        obj: object to check if type is instance of a class
        a_class: class to check if obj is an instance of
    returns:
        True if obj is an instance of a_class else False
    """
    return isinstance(obj, a_class)
