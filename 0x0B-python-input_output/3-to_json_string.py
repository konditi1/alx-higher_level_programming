#!/usr/bin/python3
import json

"""
function that returns the JSON representation of an object (string):
"""


def to_json_string(my_obj):
    """
    function that returns the JSON representation of an object (string)
    :parameter
        my_obj: object to be converted
    :return:
        the JSON representation of my_obj
    """
    return json.dumps(my_obj)
