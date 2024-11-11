#!/usr/bin/python3
"""Append a string to a text file."""


def append_write(filename="", text=""):
    """Append a string to a text file"""
    with open(filename, "a") as f:
        return f.write(text)
