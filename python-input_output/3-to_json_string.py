#!/usr/bin/python3
"""Module that defines write_file function."""


import json


def to_json_string(my_obj):
    """"Return JSON representation of an object."""

    return json.dumps(my_obj)
