#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_to_delete = []
    for key, values in a_dictionary.items():
        if key == value:
            key_to_delete.append(key)
    for key in key_to_delete:
        del a_dictionary[key]
    return a_dictionary
