#!/usr/bin/python3
def no_c(my_string):
    list_str = list(my_string)
    list_str = [char for char in list_str if char.lower() != 'c']
    new_string = ''.join(list_str)
    return new_string
