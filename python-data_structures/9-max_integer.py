#!/usr/bin/python3


def max_integer(my_list=[]):
    length = len(my_list)
    biggest = my_list[0] if length > 0 else None
    for i in range(length):
        if my_list[i] > biggest:
            biggest = my_list[i]
    return biggest
