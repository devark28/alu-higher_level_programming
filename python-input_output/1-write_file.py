#!/usr/bin/python3
"""Write a string to a text file."""


def write_file(filename="", text=""):
    """Write a string to a text file"""
    with open(filename, "w") as f:
        return f.write(text)
