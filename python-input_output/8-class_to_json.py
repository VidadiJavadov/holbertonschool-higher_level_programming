#!/usr/bin/python3
"""classtojson"""


def class_to_json(obj):
    """Represent class as json format"""
    return obj.__dict__
