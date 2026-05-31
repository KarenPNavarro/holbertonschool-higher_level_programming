#!/usr/bin/python3
"""Defines a Rectangle class based on BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle using BaseGeometry validation."""

    def __init__(self, width, height):
        """Initializes a rectangle with validated width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns the [Rectangle] <width>/<height> description."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
