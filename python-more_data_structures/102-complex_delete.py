#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    if isinstance(a_dictionary, dict):
        for d in [k for k, v in a_dictionary.items() if v == value]:
            del a_dictionary[d]
    return a_dictionary
