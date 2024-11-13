#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""


def class_to_json(obj):
    """Return the dictionary description with simple data structure."""
    props = dir(obj)
    dict_property = {}
    for p in props:
        attr = getattr(obj, p)
        if not callable(attr) and not p.startswith("__"):
            dict_property[p] = attr
    return dict_property


class Student:
    """A student class."""

    def __init__(self, first_name, last_name, age):
        """Initialize student class."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """class to json"""
        return class_to_json(self)
