#!/usr/bin/python3


def no_c(my_string):
    new_string = ''
    for c in range(my_string.__len__()):
        if not (my_string[c] == 'c' or my_string[c] == 'C'):
            new_string += my_string[c]
    return new_string
# print(no_c("School Chicken"))
