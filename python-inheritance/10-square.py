#!/usr/bin/python3
"""A file contains Square1 class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class for square"""
    def __init__(self, size):
        """Initialization of Square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size,size)

    def area(self):
        """Area"""
        return self.__size ** 2
