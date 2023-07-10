#!/usr/bin/python3
"""
function which returns True if the object is an instance of a
class else False
"""


def is_same_class(obj, a_class):
    """
    function which returns True if the object is an instance of
    a class else False
    parameter:
        obj: object to check if type is instance of a class
        a_class: class to check if obj is an instance of
    returns:
        True if obj is an instance of a_class else False
    """
    return type(obj) is a_class
