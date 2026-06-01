#!/usr/bin/python3
"""Defines an abstract Animal class with Dog and Cat subclasses."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Abstract method: subclasses must return the animal's sound."""


class Dog(Animal):
    """Represents a dog."""

    def sound(self):
        """Returns the dog's sound."""
        return "Bark"


class Cat(Animal):
    """Represents a cat."""

    def sound(self):
        """Returns the cat's sound."""
        return "Meow"
