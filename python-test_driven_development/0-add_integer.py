#!/usr/bin/python3
"""
Function add integer
"""


def add_integer(a, b=98):
    """
    Function that adds 2 numbers
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    print(add_integer(1.1))
