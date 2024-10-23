#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    if isinstance(a_dictionary, dict) and value in a_dictionary.values():
        map(lambda x: x, [k for k, v in a_dictionary.items() if v == value])
