#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > my_list.__len__() - 1:
        return my_list 
    else:
        return list(
            map(
                lambda tp: tp[1], filter(
                    lambda num: num[0] != idx, list(
                        enumerate(my_list)))))