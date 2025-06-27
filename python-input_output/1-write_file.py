#!/usr/bin/python3
"""writig files"""


def write_file(filename="", text=""):
    """function"""
    with open(filename, mode = "w", encoding = "utf-8") as f:
        return f.write(text)
