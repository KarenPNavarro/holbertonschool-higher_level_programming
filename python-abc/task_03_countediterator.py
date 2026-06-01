#!/usr/bin/python3
"""Defines a CountedIterator that counts iterated items."""


class CountedIterator:
    """An iterator wrapper that counts how many items were fetched."""

    def __init__(self, iterable):
        """Initializes the underlying iterator and a counter."""
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """Returns the iterator object itself."""
        return self

    def __next__(self):
        """Fetches the next item, counts it, and returns it."""
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Returns the number of items fetched so far."""
        return self.count
