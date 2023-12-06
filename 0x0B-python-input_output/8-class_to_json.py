#!/usr/bin/python3
"""Convert an object to a dictionary with a simple data
structure for JSON serialization."""


def class_to_json(obj):
    """
    Convert an object to a dictionary with a simple
    data structure for JSON serialization.

    Args:
        obj: Instance of a class with serializable attributes.

    Returns:
        dict: Dictionary representation of the object.
    """
    # Get all attributes of the object
    attributes = obj.__dict__

    # Create a dictionary to store the serializable attributes
    serializable_dict = {}

    # Iterate through the attributes
    for key, value in attributes.items():
        # Check if the attribute value is of a serializable type
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_dict[key] = value

    return serializable_dict
