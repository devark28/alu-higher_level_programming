#!/usr/bin/python3


def uppercase(text):
    charsBag = str(text).split("")
    print(charsBag)
    res = ""
    for c in charsBag:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            translation = ord(c) - ord('a')
            res += chr(ord('A') + translation)
        else:
            res += c
    return res

uppercase("Holberton School 98 Battery street")
