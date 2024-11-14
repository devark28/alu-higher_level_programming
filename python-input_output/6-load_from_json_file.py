#!/usr/bin/python3
"""Load a JSON string from a file."""
import json


def load_from_json_file(filename):
    """Load a JSON string from a file."""
    with open(filename, "r") as f:
        dict_date = json.loads(f.read())
        return dict_date
