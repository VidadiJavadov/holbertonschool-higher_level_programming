#!/usr/bin/python3
"""Create an object from json file"""
import json


def load_from_json_file(filename):
    """function"""
    with open(filename) as mf:
        obj = json.load(mf)
