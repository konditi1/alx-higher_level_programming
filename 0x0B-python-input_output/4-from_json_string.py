#!/usr/bin/python3

"""
from json string to object
"""
import json


def from_json_string(my_str):
    """
    function that returns an object python represented by json string
    :parameter
        ny_string: json string
    :return:
        the object python represented by json string
    """
    return json.loads(my_str)
