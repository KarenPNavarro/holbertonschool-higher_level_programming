#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """A list subclass that can print its elements sorted."""

    def print_sorted(self):
        """Prints the list's elements in ascending order."""
        print(sorted(self))
        