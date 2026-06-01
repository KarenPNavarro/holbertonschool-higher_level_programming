#!/usr/bin/python3
"""Defines Shape, Circle, Rectangle and a shape_info function."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Abstract method: return the shape's area."""

    @abstractmethod
    def perimeter(self):
        """Abstract method: return the shape's perimeter."""


class Circle(Shape):
    """Represents a circle defined by its radius."""

    def __init__(self, radius):
        """Initializes the circle with a radius."""
        self.radius = radius

    def area(self):
        """Returns the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Returns the circle's perimeter (circumference)."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Represents a rectangle defined by width and height."""

    def __init__(self, width, height):
        """Initializes the rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Prints the area and perimeter of any shape-like object."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
