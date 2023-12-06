#!/usr/bin/python3
"""Represent class student."""


class Student:
    """
    Retrieves a dictionary representation of a Student instance.

    Returns:
        dict: A dictionary containing the public attributes of
        the Student instance.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
