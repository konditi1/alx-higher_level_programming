#!/usr/bin/python3
"""
 function that returns True if the object is an instance
 of a class that inherited (directly or indirectly)
 from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
    function that returns True if the object is an instance of a
    class that inherited (directly or indirectly)
    from the specified class ; otherwise False.
    parameter:
        obj: object to check if type is instance of a class
        a_class: class to check if obj is an instance of
    returns:
        True if obj is an instance of a_class else False
    """
    return isinstance(obj, a_class) and type(obj) != a_class
