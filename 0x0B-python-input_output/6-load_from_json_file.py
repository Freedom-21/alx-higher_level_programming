#!/usr/bin/python3
""" load """

import json

def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        object: The Python object loaded from the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
