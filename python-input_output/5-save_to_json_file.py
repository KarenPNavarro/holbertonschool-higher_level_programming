#!/usr/bin/python3
"""Module that defines save_to_json_file function."""


import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
