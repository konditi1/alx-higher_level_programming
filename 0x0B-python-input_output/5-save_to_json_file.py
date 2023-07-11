#!/usr/bin/python3
"""
writes an object to a text file using json rep
"""
import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an object to a text file using json rep
    :param :
        my_obj: object to be converted
    :param :
        filename: name of the file to be created
    :return:
    the filename of the created file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(json.dumps(my_obj))
