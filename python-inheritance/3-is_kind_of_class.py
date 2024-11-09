#!/usr/bin/python3
"""is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of a_class or a class that inherited
    from a_class"""
    return isinstance(obj, a_class)
