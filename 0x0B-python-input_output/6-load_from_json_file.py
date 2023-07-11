#!/usr/bin/python3
"""
function that creates an object from a json file
"""
import json


def load_from_json_file(filename):
    """
    function that creates an object from a json file
    :param :
        filename: name of the file to be created
    :return:
        the object python represented by json string
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
