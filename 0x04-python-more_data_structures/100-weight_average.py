#!/usr/bin/python3
def weight_average(my_list=None):
    if my_list is None:
        my_list = []
    if not my_list:
        return 0
    weighted_product = 0
    total_weight = 0

    for score, weight in my_list:
        weighted_product += score * weight
        total_weight += weight
    if total_weight == 0:
        weighted_average = 0
    else:
        weighted_average = weighted_product / total_weight
    return weighted_average
