#!/usr/bin/python3
"""Represent class student."""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of strings specifying attribute
            names to be retrieved.
                          If None, retrieve all attributes.

        Returns:
            dict: A dictionary containing the specified attributes of
            the Student instance.
        """
        if attrs is None:
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }

        result_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                result_dict[attr] = getattr(self, attr)
        return result_dict
