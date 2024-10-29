#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    num = ""
    count = 0
    try:
        for i in range(x):
            num += str(my_list[i])
            count += 1
    except:
        pass
    print("{:d}".format(int(num)))
    return count
