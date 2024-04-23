#!/usr/bin/python3
"""Module for Base class"""


class Base:
    """Base class to manage id attribute in future classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id (int): The id of the instance. If None, a new id is assigned.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
