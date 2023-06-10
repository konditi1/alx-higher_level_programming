#!/usr/bin/python3
def max_integer(my_list=None):
    if not my_list:
        return None
    biggest_int = my_list[0]
    if not my_list:
        return None
    if isinstance(my_list, list):
        for item in my_list:
            if item > biggest_int:
                biggest_int = item
        return biggest_int
