#!/usr/bin/python3
import json
"""Serialization"""


def serialize_and_save_to_file(data, filename):
    """Ser_and_save"""
    with open(filename, mode="w") as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """load_and_deser"""
    with open(filename, mode="r") as file:
        data = json.load(file)
        return data
