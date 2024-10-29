#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    try:
        print("{:d}", my_list[:x], end="")
        print()
    except Exception as e:
        pass
