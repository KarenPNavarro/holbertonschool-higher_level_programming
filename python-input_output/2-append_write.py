#!/usr/bin/python3
"""Module that defines write_file function."""


def append_write(filename="", text=""):
    """Write a function that appends a string at the end of a text file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
