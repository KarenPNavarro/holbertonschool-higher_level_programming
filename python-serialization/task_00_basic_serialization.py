#!/usr/bin/python3
"""Module that defines serialization and deserialization functions."""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary and save it to a JSON file."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(data))


def load_and_deserialize(filename):
    """Load and deserialize a JSON file to a Python dictionary."""
    with open(filename, encoding="utf-8") as f:
        return json.loads(f.read())
