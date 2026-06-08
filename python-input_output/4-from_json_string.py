#!/usr/bin/python3
"""Module that defines write_file function."""


import json


def from_json_string(my_str):
    """"Write a function that returns an object by a JSON string."""

    return json.loads(my_str)
