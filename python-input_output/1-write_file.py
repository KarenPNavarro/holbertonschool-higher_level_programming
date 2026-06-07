#!/usr/bin/python3
"""Module that defines write_file function."""


def write_file(filename=""):
    """Write a text file and print it."""
    with open(filename, encoding="utf-8") as f:
        print(f.write(), end="")
