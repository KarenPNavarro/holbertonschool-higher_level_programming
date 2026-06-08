#!/usr/bin/python3
"""Module that defines load_from_json_file function."""


import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    with open(filename, encoding="utf-8") as f:
        return json.loads(f.read())
