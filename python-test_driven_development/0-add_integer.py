#!/usr/bin/python3
"""Module that defines the add_integer function.

This module provides a function that adds two integers
(or floats cast to integers). It raises TypeError for
non-numeric inputs.
"""


def add_integer(a, b=98):
    """Add two integers or floats (casted to integers).

    Raises TypeError if a or b is not an int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
