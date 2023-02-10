#!/usr/bin/python3
""" function that prints a text with 2 new lines"""


def text_indentation(text):
    """prints a text with 2 new lines"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars = [".", ":", "?"]
    prev = 0

    for i in range(len(text)):
        if i == len(text) - 1:
            print(text[prev:i + 1], end="")
        elif text[i] in chars:
            print(text[prev:i + 1], end="")
            print('\n\n')
            prev = i + 1
            while text[prev] == " ":
                prev += 1
