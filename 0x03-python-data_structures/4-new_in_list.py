#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    # list comprehension to item at given index
    new_list = [
        element if i == idx else item
        for i, item in enumerate(my_list)
    ]
    return new_list
