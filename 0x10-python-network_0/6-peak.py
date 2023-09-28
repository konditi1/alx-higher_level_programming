#!/usr/bin/python3
"""
This script defines a function find_peak to find a peak in an unsorted list of integers.
A peak is an element that is greater than its neighbors.
"""


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    Args:
        list_of_integers (list of int): List of integers.

    Returns:
        int or None: The peak integer if found, None if the list is empty.
    """
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1

    while left < right:
        mid = (left + right) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return list_of_integers[left]
