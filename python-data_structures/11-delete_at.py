#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > my_list.__len__() - 1:
        return my_list 
    else:
        my_list = list(
            map(
                lambda tp: tp[1], filter(
                    lambda num: num[0] != idx, list(
                        enumerate(my_list)))))
        return my_list
lst = [1, 2, 3, 4, 5]
print(delete_at(lst, 3))
print(lst)
