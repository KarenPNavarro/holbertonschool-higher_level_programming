#!/usr/bin/python3
"""Module that converts CSV data to JSON format."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to JSON format and write to data.json."""
    try:
        rows = []
        with open(csv_filename, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)
        with open("data.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(rows))
        return True
    except FileNotFoundError:
        return False
