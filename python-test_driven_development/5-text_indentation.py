#!/usr/bin/python3
"""Module that defines a text indentation function."""


def text_indentation(text):
    """Prints a text with 2 new lines after '.', '?' and ':'"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    n = len(text)

    while i < n:

        # skip leading spaces
        while i < n and text[i] == " ":
            i += 1

        while i < n:
            print(text[i], end="")

            if text[i] in ".?:":
                print("\n")
                i += 1

                # skip spaces AFTER punctuation
                while i < n and text[i] == " ":
                    i += 1

                break

            i += 1
