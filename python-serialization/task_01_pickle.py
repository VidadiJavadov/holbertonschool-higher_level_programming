#!/usr/bin/python3
"""Serialization using the pickle module"""

import pickle


class CustomObject:
    """Custom object with name, age, and student status"""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes"""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize the object and save it to the given file"""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (OSError, pickle.PickleError) as e:
            print("Serialization error:", e)

    @classmethod
    def deserialize(cls, filename):
        """Deserialize and return an object from the given file"""
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except (OSError, pickle.PickleError) as e:
            print("Deserialization error:", e)
            return None
