#!/usr/bin/python3
import json
import pickle
import string
"""Serialization"""


class CustomObject:
    """CustomObj"""
    name: string
    age: int
    is_student: bool

    def __init__(self, name, age, is_student):
        """init"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """display"""
        print("Name: {} \n Age: {} \n Is Student: {}".format(self.name, self.age, self.is_student))

    def serialize(self, filename):
        """serializing"""
        with open(filename, mode="wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """deserializing"""
        with open(filename, mode="rb") as file:
            return (pickle.load(file))
