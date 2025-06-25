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

    def area(self):
        """Method for calculating area of rectangle"""

        return self.__width * self.__height

    def perimeter(self):
        """This a method for calculating perimetr of a rectangle"""

        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width + self.__height) * 2
    
    def __str__(self):
        """Return rectangle as a string of '#' characters"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for i in range(self.__height)])
    
    def __repr__(self):
        """Returning string"""

        return "Rectangle({}, {})".format({self.__width, self.__height})
