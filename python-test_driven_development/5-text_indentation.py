#!/usr/bin/python3
""" function that prints a text with 2 new lines"""


def text_indentation(text):
    """prints a text with 2 new lines"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars = [".", ":", "?"]

    for aux, i in enumerate(text):
        if i in chars:
            print(i, end="\n")
            print()

        elif i == " ":
            if text[aux-1] in chars:
                continue
            else:
                print(i, end="")

        else:
            print(i, end="")
