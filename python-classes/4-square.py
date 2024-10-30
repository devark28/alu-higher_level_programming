#!/usr/bin/python3
"""
an empty Square class
"""


class Square:
    """
    Square class
    """
    def __init__(self, value=0):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        return self.__size ** 2
    def size(self):
        return self.__size
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
