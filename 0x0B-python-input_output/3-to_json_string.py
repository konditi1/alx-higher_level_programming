#!/usr/bin/python3

"""
function that returns the JSON representation of an object (string):
"""
import json


def to_json_string(my_obj):
    """
    function that returns the JSON representation of an object (string)
    :parameter
        my_obj: object to be converted
    :return:
        the JSON representation of my_obj
    """
    return json.dumps(my_obj)
