#!/usr/bin/python3
"""This is a object to file function"""
import json


def save_to_json_file(my_obj, filename):
    """func"""
    with open(filename, mode="w") as myfile:
        json.dumbs(my_obj, myfile)
