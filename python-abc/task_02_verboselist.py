#!/usr/bin/python3
"""Defines a VerboseList class that announces list modifications."""


class VerboseList(list):
    """A list that prints a message on add/remove operations."""

    def append(self, item):
        """Appends item, then prints a notification."""
        super().append(item)
        print("Added {} to the list.".format(item))

    def extend(self, iterable):
        """Extends the list, then prints how many items were added."""
        items = list(iterable)
        super().extend(items)
        print("Extended the list with {} items.".format(len(items)))

    def remove(self, item):
        """Prints a notification, then removes the item."""
        print("Removed {} from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Prints a notification, then pops and returns the item."""
        print("Popped {} from the list.".format(self[index]))
        return super().pop(index)
