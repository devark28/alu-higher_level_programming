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
    char = 0
    while char < len(text) and text[char] == ' ':
        char += 1

    while char < len(text):
        new_text += text[char]
        if text[char] == "\n" or text[char] in ".?:":
            if text[char] in ".?:":
                new_text += "\n\n"
            char += 1
            while char < len(text) and text[char] == ' ':
                char += 1
            continue
        char += 1
    print(new_text, end="")

# text_indentation("Holberton. School? How are you: John")
