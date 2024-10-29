#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    try:
        print(int("".join(str(my_list[i]) for i in range(x))))
    except Exception as e:
        pass
