#!/usr/bin/python3
"""
This module provides utility functions for arithmetic operations.
Currently, it contains a function to add two integers.
"""

def add_integer(a, b=98):
    """
    Add two integers or floats.
    The function casts floats into integers before addition.
    
    Args:
    a (int, int): The first number, must be an integer or float.
    b (int, int, optional): The second number, must be an integer or float. Defaults to 98.

    Returns:
    int: The sum of a and b after casting them to integers.

    Raises:
    TypeError: If either a or b is not an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
