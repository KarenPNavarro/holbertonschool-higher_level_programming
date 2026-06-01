#!/usr/bin/python3
"""Demonstrates mixins with SwimMixin, FlyMixin and Dragon."""


class SwimMixin:
    """Mixin that adds swimming ability."""

    def swim(self):
        """Prints that the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying ability."""

    def fly(self):
        """Prints that the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A dragon that can swim and fly via mixins."""

    def roar(self):
        """Prints that the dragon roars."""
        print("The dragon roars!")
