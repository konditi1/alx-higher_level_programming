#!/usr/bin/python3
"""
a class representing students
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
        Initializes a student object with the provided attributes.
        to_json(self, attrs=None): Retrieves a dictionary representation
        of the student instance.

    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a student object with the provided first name,
        last name, and age.

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
            attrs (list, optional):list of attr names to be included dict repr
                If None or not list, all attri are included. Defaults to None.

        Returns:
            dict: A dict containing the requested attr and their values.

        """
        if attrs is None or not isinstance(attrs, list):
            # Return all attributes if attrs is None or not a list
            return self.__dict__
        else:
            # Return only the requested attributes
            json_dict = {}
            for attr in attrs:
                if attr in self.__dict__:
                    json_dict[attr] = self.__dict__[attr]
            return json_dict
