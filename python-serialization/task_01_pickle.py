#!/usr/bin/python3
import pickle
"""Serialization"""


class CustomObject:
    """CustomObj"""
    def __init__(self, name, age, is_student):
        """init"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """display"""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize the object to a binary file using pickle"""
        try:
            with open(filename, mode="wb") as file:
                pickle.dump(self, file)
        except (OSError, pickle.PickleError) as e:
            print("Serialization error:", e)

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a binary file using pickle"""
        try:
            with open(filename, mode="rb") as file:
                return pickle.load(file)
        except (OSError, pickle.PickleError) as e:
            print("Deserialization error:", e)
            return None
