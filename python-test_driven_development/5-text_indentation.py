#!/usr/bin/python3
def text_indentation(text):
    """Prints a text with 2 new lines after '.', '?' and ':'"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""

    for char in text:
        new_text += char

        if char in ".?:":
            new_text += "\n\n"

    lines = new_text.split("\n")

    for line in lines:
        print(line.strip())
