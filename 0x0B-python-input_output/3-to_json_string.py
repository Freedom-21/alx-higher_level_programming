#!/usr/bin/python
""" json """
import json

def to_json_string(my_obj):
    """
    Returns the JSON representation of an object

    Args:
        my_obj: an input object
    """

    return json.dumps(my_obj)
