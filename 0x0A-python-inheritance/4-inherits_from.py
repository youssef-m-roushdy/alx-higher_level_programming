#!/usr/bin/python3
"""Method check inherits from class."""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    :param obj: The object to check.
    :param a_class: The class to check against.
    :return: True if the object is an instance of a class that inherited
             from the specified class; otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
