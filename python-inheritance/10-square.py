#!/usr/bin/python3
"""Defines a Square class based on Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size):
        """Initializes a square with a validated size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
