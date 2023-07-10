#!/usr/bin/python3
"""
mylist class which inherits from list
"""


class MyList(list):
    """
    mylist class which inherits from list
    """

    def print_sorted(self):
        """prints the list in ascending order"""
        print(sorted(self))
