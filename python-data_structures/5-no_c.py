#!/usr/bin/python3


def no_c(my_string):
    new_string = ''
    for c in range(my_string.__len__()):
        if not (my_string[c] == 'c' or c == 'C'):
            new_string += my_string[c]
    return my_string
no_c("School")
