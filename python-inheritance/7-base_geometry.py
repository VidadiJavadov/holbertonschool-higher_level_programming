#!/usr/bin/python3
"""This file contains a class named BaseGeometry"""


class BaseGeometry:
    """BaseGeometry class"""
    
    def area(self):
        """A method for area"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """A method for validating"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("<{} must be greater than 0".format(name))
