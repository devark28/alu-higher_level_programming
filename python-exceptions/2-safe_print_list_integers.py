#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    try:
        num = ""
        count = 0
        for i in range(x):
            num += str(my_list[i])
            count += 1
        print("{:d}".format(num))
        return count
    except:
        pass
