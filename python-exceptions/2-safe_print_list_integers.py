#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    num = ""
    count = 0
    try:
        for i in range(x):
            num += str(my_list[i])
            count += 1
        print("{:d}".format(int(num)))
    except:
        pass
    return count
