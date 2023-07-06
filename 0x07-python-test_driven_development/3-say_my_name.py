#!/usr/bin/python3
"""
module which contains the function say_my_name
"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name prints the person's name
       param first_name: str
          the person's first name
       param last_name: str
           the person's last name
       return: None
    """

    try:
        if first_name == "" and last_name == "":
            raise ValueError("first_name and last_name must not be empty")
        if not isinstance(first_name, str):
            raise TypeError("first_name must be a string")
        if not isinstance(last_name, str):
            raise TypeError("last_name must be a string")
        print(f"My name is {first_name} {last_name}")
    except (TypeError, ValueError) as e:
        print(e)
