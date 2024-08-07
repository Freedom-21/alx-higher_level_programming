#!/usr/bin/python3
""" class student """

class Student:
    """
    Defines a student.
    """
    def __init__(self, first_name, last_name, age):
        """
        Instantiates a Student with first_name, last_name, and age.
        
        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.
        
        Returns:
            dict: A dictionary containing all the public attributes of the Student instance.
        """
        return self.__dict__

