#!/usr/bin/python3
"""funtion"""


def append_write(filename="", text=""):
    """func"""
    with open(filename, mode="a", encoding="utf-8") as myfile:
        return myfile.write(text)
