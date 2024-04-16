#!/usr/bin/python3
""" class student """

class Student:
    """
    Defines a student by first name, last name, and age.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only attributes contained in this list are retrieved.

        Args:
            attrs (list): Optional list of strings representing names of attributes to retrieve.

        Returns:
            dict: A dictionary containing specified attributes of the Student instance.
        """
        if isinstance(attrs, list) and all(isinstance(item, str) for item in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with values from the json dictionary.

        Args:
            json (dict): A dictionary with keys that match the attributes of the Student instance.
        """
        for key in json:
            if hasattr(self, key):
                setattr(self, key, json[key])

