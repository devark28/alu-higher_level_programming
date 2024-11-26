#!/usr/bin/python3
"""
This function prints a text with 2 new lines after each '.', '?', and ':'
"""


def text_indentation(text):
    """
    2 new lines after each '.', '?', and ':'
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.strip()
    if text == "":
        return
    for i in range(len(text)):
        if text[i] in [".", "?", ":"]:
            print(text[i])
            print()
        else:
            print(text[i], end="")
