#!/usr/bin/python3
"""Module that defines the print_square function.

This module provides a function that prints a square of '#'
characters with a given size. Raises TypeError for non-integer
sizes and ValueError for negative sizes.
"""


def print_square(size):
    """Print a square of size x size using '#'.

    Raises TypeError if size is not an integer.
    Raises ValueError if size is negative.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
