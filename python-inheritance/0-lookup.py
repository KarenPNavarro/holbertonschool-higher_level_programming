#!/usr/bin/python3
"""Defines a function that lists an object's attributes and methods."""


def lookup(obj):
    """Returns the list of available attributes and methods of an object."""
    return dir(obj)
