#!/usr/bin/python3


def uppercase(text):
    res = ""
    for c in text:
        if 'a' <= c <= 'z':
            translation = ord(c) - ord('a')
            res += chr(ord('A') + translation)
        else:
            res += c
    return res
