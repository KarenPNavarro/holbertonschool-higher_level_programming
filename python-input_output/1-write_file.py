#!/usr/bin/python3
"""Module that defines write_file function."""


def write_file(filename="", text=""):
    """Write a text file and print it."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
