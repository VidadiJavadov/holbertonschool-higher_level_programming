#!/usr/bin/python3

"""Rectangle Class"""


class Rectangle:
    """This a Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initializing"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter - width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter - width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter - height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter - height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
