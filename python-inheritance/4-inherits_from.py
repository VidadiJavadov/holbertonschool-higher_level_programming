#!/usr/bin/python3

"""checking inherit"""

def inherits_from(obj, a_class):
    """checks it with func"""
    return isinstance(obj, a_class) and type(obj) is not a_class
