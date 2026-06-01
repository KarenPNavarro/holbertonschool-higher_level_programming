#!/usr/bin/python3
"""Defines a MyInt class that inverts == and !=."""


class MyInt(int):
    """A rebellious int with inverted == and != operators."""

    def __eq__(self, other):
        """Returns the inverted equality (behaves like !=)."""
        return int(self) != other

    def __ne__(self, other):
        """Returns the inverted inequality (behaves like ==)."""
        return int(self) == other
