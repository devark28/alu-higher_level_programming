#!/usr/bin/python3


def remove_char_at(str="noy", n=1):
    res = ""
    for i in range(len(str)):
        if i != n:
            res += str[i]
    print(f"{res}")
    return res
