#!/usr/bin/python3
"""
class representing students
"""


class Student:
    """
    A class representing a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.

    Methods:
        __init__(self, first_name, last_name, age):
        Initializes a student object.
        to_json(self, attrs=None): Retrieves a dictionary
        representation of the student instance.
        reload_from_json(self, json):
         Replaces all attributes of the student instance.

    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a student object.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.

        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the student instance.

        Args:
            attrs (list, optional): A list of attribute names to be included
            Defaults to None.

        Returns:
            dict: A dictionary containing the requested attributes
            and their values.

        """

        if attrs is None or not isinstance(attrs, list):
            return self.__dict__
        else:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the student instance.

        Args:
            json (dict):dict containing attribute names and their values.

        """

        for key, value in json.items():
            setattr(self, key, value)
