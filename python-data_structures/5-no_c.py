#!/usr/bin/python3


def no_c(my_string):
    for c in range(my_string.length):
        if my_string[c] == 'c' or c == 'C':
            my_string[c] = ''
    return my_string
