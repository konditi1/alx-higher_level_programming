#!/usr/bin/python3
"""
script that adds all arguments to a python list
and saves them to file
"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_arguments_to_list(args):
    """ Load existing data from the file"""
    try:
        existing_data = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_data = []

    """Add arguments to the existing data"""
    existing_data.extend(args)

    """ Save the updated data to the file"""
    save_to_json_file(existing_data, "add_item.json")


"""Get arguments passed to the script (excluding the script name)"""


arguments = sys.argv[1:]


"""Add the arguments to the list and save them to the file"""
add_arguments_to_list(arguments)
