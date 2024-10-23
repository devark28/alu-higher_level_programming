#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    return my_list if idx < 0 or idx > my_list.__len__() - 1 else filter(lambda _, i: i != idx, enumerate(my_list))
