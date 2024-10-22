#!/usr/bin/python3


def uppercase(text):
    res = ""
    for c in text:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            translation = ord(c) - ord('a')
            res += chr(ord('A') + translation)
        else:
            res += c
    print("{}".format(res))
