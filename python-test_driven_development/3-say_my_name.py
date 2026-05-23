#!/usr/bin/python3
"""Module that defines the say_my_name function.

This module provides a function that prints a greeting using
a person's first and last name. Raises TypeError for non-string
inputs.
"""


def say_my_name(first_name, last_name=""):
    """Print 'My name is <first_name> <last_name>'.

    Raises TypeError if first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
