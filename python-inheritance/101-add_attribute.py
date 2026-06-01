#!/usr/bin/python3
"""Defines a function that adds an attribute to an object if allowed."""


def add_attribute(obj, name, value):
    """Adds attribute name=value to obj, or raises TypeError."""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
