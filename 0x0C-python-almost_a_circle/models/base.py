#!/usr/bin/python3
"""
base class
"""
import json


class Base:
    """
    base class
    """
    __nb_objects = 0
    """
    a private class attribute __nb_objects for tracking
    the number of objects created
    """

    def __init__(self, id=None):
        """
        constructor for the base class
        param:
            id: id of the object
        return:
            nothing
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        function that returns the JSON representation of an object (string):
        return:
            the JSON representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        function that writes an object to a text file using json rep
        :param list_objs:
        :return:
        """
        if list_objs is None or len(list_objs) == 0:
            text = "[]"
        else:
            list_objs = [cls.to_dictionary(obj) for obj in list_objs]
            text = cls.to_json_string(list_objs)
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(text)

    def from_json_string(json_string):
        """
        function that returns an object python represented by json string
        :param json_string:
        :return:
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        function that returns an instance with all attributes already set
        :param dictionary:
        :return:
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        function that returns a list of instances
        :return:
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                objects = cls.from_json_string(f.read())
                instances = []
                for obj in objects:
                    if cls.__name__ == "Rectangle":
                        instance = cls(obj['width'], obj['height'],
                                       obj['x'], obj['y'], obj['id'])
                    elif cls.__name__ == "Square":
                        instance = cls(obj['size'], obj['x'],
                                       obj['y'], obj['id'])
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []
