#!/usr/bin/python3
""" function that prints a text with 2 new lines"""


def text_indentation(text):
    """prints a text with 2 new lines"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars = [".", ":", "?"]
    skip_next = False
    
    for idx, i in enumerate(text):
        if skip_next:
            skip_next = False
            continue

        if i in chars:
            print(i, end="\n")
            print()
            skip_next = True

        else:
            print(i, end="")
