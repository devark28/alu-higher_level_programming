#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    try:
        num = ""
        count = 0
        for i in range(x):
            num += str(my_list[i])
            count += 1
        print(num)
        return count
    except Exception as e:
        pass
