#!/usr/bin/python3
"""Module that defines a text indentation function."""


def text_indentation(text):
    """Prints a text with 2 new lines after '.', '?' and ':'"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    length = len(text)

    while i < length:

        # skip leading spaces
        while i < length and text[i] == " ":
            i += 1

        while i < length:
            print(text[i], end="")

            if text[i] in ".?:":
                print("\n")
                i += 1
                break

            i += 1
