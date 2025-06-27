#!/usr/bin/python3
"""this file contains a read_file function"""


def read_file(filename=""):
    """This is that function which prints content of file"""

    with open(filename, encoding="utf-8") as myfile:
        print(myfile.readlines())
