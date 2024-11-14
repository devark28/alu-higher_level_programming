#!/usr/bin/python3
"""Save an object to a file as JSON."""
import json


def save_to_json_file(my_obj, filename):
    """Save an object to a file as JSON."""
    with open(filename, "w") as f:
        json_data = json.dumps(my_obj)
        f.write(json_data)
