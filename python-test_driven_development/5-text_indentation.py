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
    new_text = ""
    for i in text:
        new_text += i
        if i == '.' or i == '?' or i == ':':
            new_text += "\n\n"
    print(new_text, end="")
