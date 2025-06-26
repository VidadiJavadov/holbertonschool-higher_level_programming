#!/usr/bin/python3
"""This file defines a Rectangle class that inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """Initialize with width and height (validated)."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """A method for calculating are"""
        return self.__width * self.__height
    
    def print(self):
        """A method for print"""
        print("[Rectangle] {}/{}".format(self.__width, self.__height))

    def __str__(self):
        """a methd for returning w/h"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
