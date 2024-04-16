#!/usr/bin/python3
""" class to json """

def class_to_json(obj):
    """
    Returns the dictionary description with simple data structures suitable for JSON serialization of an object.

    Args:
        obj: An instance of a class with possibly serializable attributes.

    Returns:
        A dictionary of the object's attributes that are serializable.
    """
    return obj.__dict__
