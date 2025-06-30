#!/usr/bin/python3
import pickle
"""Serialization"""


class CustomObject:
    """CustomObj"""
    name: str
    age: int
    is_student: bool

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
        """serializing"""
        with open(filename, mode="wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """deserializing"""
        with open(filename, mode="rb") as file:
            return pickle.load(file)
