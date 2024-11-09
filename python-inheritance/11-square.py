#!/usr/bin/python3
"""Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Initializes a Square object"""
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculates the area of the Square"""
        return self.__size ** 2

    def __str__(self):
        """Returns a string representation of the Square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
