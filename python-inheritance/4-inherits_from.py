#!/usr/bin/python3
"""Defines a function checking indirect or direct inheritance."""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a subclass of a_class."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
