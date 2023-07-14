#!/usr/bin/python3
"""
function that returns dictionary rep with simple structure
"""


def class_to_json(obj):
    """
    Convert an object to a dictionary with a
    simple data structure for JSON serialization.

    Args:
        obj: An object instance of a class.

    Returns:
        dict: A dictionary containing the serializable
        attributes of the object.

    """
    json_dict = {}

    # Iterate over the attributes of the object
    for attr in obj.__dict__:
        value = obj.__dict__[attr]

        # Check if the attribute value is of a serializable type
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[attr] = value

    return json_dict
