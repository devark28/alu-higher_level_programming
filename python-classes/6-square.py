#!/usr/bin/python3
"""
an empty Square class
"""


class Square:
    """
    Square class
    """
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if (not isinstance(position, tuple) or len(position) != 2 or
                not all(isinstance(x, int) and x >= 0 for x in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def my_print(self):
        for i in range(self.__size):
            if i == 0:
                print("\n" * self.__position[1], sep="", end="")
            print(" " * self.__position[0] + "#" * self.__size,
                  end="\n" if i < self.__size - 1 else "")
        print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if (not isinstance(position, tuple) or len(position) != 2 or
                not all(isinstance(x, int) and x >= 0 for x in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
