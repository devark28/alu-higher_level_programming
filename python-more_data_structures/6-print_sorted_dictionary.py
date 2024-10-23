#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    print(f"{k}: {a_dictionary[k]}" for k in list(sorted(a_dictionary.keys())))
