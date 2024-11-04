#!/usr/bin/python3
"""
an empty Rectangle class
"""


class Rectangle:
    """
    Rectangle class
    """
    number_of_instances = 0  # number of instances of Rectangle
    print_symbol = "#"  # symbol used for string representation

    def __init__(self, width=0, height=0):
        """
        initializes the Rectangle class
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """
        returns the width of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        sets the width of the Rectangle
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """
        returns the height of the Rectangle
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        sets the height of the Rectangle
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """
        returns the area of the Rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        returns the perimeter of the Rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        returns the string representation of the Rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([
            str(self.print_symbol) * self.__width for i in range(self.__height)
            ])

    def print(self):
        """
        prints the string representation of the Rectangle
        """
        print(str(self))

    def __repr__(self):
        """
        returns the string representation of the Rectangle
        to be able to recreate a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        prints a message when an instance of Rectangle is deleted
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    def square(size=0):
        return Rectangle(size, size)
