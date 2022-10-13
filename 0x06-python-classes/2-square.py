#!/usr/bin/python3
"""Defines a class Square"""
class Square:
    """create a template for instances"""
    def __init__(self, size=0):
        """instatiation of new instance
        size:
            instance attribute of int type
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise = ValueError("size must be >= 0")
        self.__size = size
