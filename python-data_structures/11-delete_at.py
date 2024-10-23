#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > my_list.__len__() - 1:
        return my_list 
    else:
        (x, y) = list(filter(lambda _, i: i != idx, list(
            enumerate(my_list))))
        return (x, y)
