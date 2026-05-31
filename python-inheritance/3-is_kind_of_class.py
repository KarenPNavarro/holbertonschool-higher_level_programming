#!/usr/bin/python3
"""Defines a function checking instance or subclass membership."""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of a_class or a subclass."""
    return isinstance(obj, a_class)
