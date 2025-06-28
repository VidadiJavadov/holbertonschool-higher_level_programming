#!/usr/bin/python3
"""Student"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """init method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dict representation"""
        result = {}
        if isinstance(attrs, list):
            for attr in attrs:
                if (type(attr) is str):
                    for key in attrs:
                        if hasattr(self, key):
                            result[key] = getattr(self, key)
        return self.__dict__
    
    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        with those from the json dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
