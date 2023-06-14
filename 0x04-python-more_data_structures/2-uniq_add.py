#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = list(set(my_list))
    total = 0
    for item in new_list:
        total += item
    return total
