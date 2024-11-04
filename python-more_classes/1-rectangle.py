#!/usr/bin/python3
"""
an empty Rectangle class
"""


class Rectangle:
    """
    Rectangle class
    """
    def __init__(self, width=0, height=0):
        """
        initializes the Rectangle class
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        returns the width of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the width of the Rectangle
        """
        self.__width = value

    @property
    def height(self):
        """
        returns the height of the Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the height of the Rectangle
        """
        self.__height = value
