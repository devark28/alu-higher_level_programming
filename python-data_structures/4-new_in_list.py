#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if idx < 0 or idx > my_list.__len__() - 1:
      return my_list
    else:
      my_list[idx] = element
      return my_list
