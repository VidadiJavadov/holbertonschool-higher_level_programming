#!/usr/bin/python3
"""Create an object from json file"""
import json


def load_from_json_file(filename):
    """func"""
    with open(filename, mode="r", encoding="utf-8") as myfile:
        return json.load(myfile)
