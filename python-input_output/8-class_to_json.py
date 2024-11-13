#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""


def class_to_json(obj):
    """Return the dictionary description with simple data structure."""
    props = dir(obj)
    dict_property = {}
    for p in props:
        dict_property[p] = obj.__getattribute__(p)
    return dict_property
