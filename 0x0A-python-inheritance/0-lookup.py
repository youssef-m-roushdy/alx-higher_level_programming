#!/usr/bin/python3
"""Method to lookup"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    :param obj: The object to inspect.
    :return: A list of strings representing attributes and methods.
    """
    return [attr for attr in dir(obj)]
