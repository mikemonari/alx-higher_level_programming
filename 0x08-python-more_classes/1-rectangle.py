#!/usr/bin/python3
"""
class Rectangle which defines a rectangle
"""
class Rectangle:
    """Rectangle that made by width and height"""
    def __init__(self, width, height):
        """initializing the objects"""
        self.__width = width
        self.__height = height
    @property
    def width(self):
        """gets the width of the rectangle object"""
        return self.__width
    @width.setter
    def width(self, value):
        """sets width of the Rectanle object"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets the height of the Rectangle object"""
        return self.__height
    @height.setter
    def height(self, value):    
    """Sets the height of the Rectangle object"""
    if not isinstance(value, int):
        raise TypeError("width must be an integer")
    if value < 0:
        raise ValueError("width must be >= 0")
    self.__height = value
