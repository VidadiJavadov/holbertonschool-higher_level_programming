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
