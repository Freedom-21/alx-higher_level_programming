#!/usr/bin/python3
""" save """

import json

def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj (any): The Python object to serialize.
        filename (str): The name of the file where the JSON data should be stored.

    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
