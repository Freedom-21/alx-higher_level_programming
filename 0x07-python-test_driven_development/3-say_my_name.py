#!/usr/bin/python3

"""
This module defines a function that prints the full name of a person.
"""

def say_my_name(first_name, last_name=""):

    """
    Print a full name.

    Args:
    first_name (str): The first name of the person.
    last_name (str, optional): The last name of the person. Defaults to an empty string.

    Raises:
    TypeError: If either first_name or last_name is not a string.

    Returns:
    None: Outputs the full name to stdout.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}".strip())
