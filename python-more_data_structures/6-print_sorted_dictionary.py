#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    if isinstance(a_dictionary, dict):
        for k in list(sorted(a_dictionary.keys())):
            print(f"{k}: {a_dictionary[k]}")
        # print(f"{k}: {a_dictionary[k]}" for k in list(
        #     sorted(a_dictionary.keys())))
