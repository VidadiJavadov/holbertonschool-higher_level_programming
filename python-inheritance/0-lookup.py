#!/usr/bin/python3

"""This is method that returns all atrs and methods in a class"""

def lookup(obj):
    """This a method which is mentioned"""
    return sorted(obj.__dict__)
