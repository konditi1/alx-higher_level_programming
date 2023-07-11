#!/usr/bin/python3
"""
class rep students
"""


class Student:
    """
    A class representing a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.

    Methods:
        to_json(): Retrieves dict repr of the student instance.

    """

    def __init__(self, first_name, last_name, age):
        """
        Init student object with provided f.name, l.name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieve a dictionary repr of  student instance.

        Returns:
            dict: A dict containing serializable attrib of the student.

        """
        json_dict = {}

        # Iterate over the attributes of the student object
        for attr in self.__dict__:
            value = self.__dict__[attr]

            # Check if the attribute value is of a serializable type
            if isinstance(value, (str, int)):
                json_dict[attr] = value

        return json_dict
