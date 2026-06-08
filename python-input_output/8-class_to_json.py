#!/usr/bin/python3
"""Module that defines class_to_json function."""


def class_to_json(obj):
    """Return dictionary description for JSON serialization of an object."""
    return obj.__dict__
