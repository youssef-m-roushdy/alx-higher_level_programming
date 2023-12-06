#!/usr/bin/python3
import json
"""Method save_to_json_file."""


def save_to_json_file(my_obj, filename):
    """
    Saves a Python object to a JSON file.

    Args:
        my_obj: The Python object to be serialized and saved to the file.
        filename (str): The name of the file where the object will be saved.

    Returns:
        None

    Raises:
        TypeError: If the object cannot be serialized to JSON.
        IOError: If an error occurs while writing to the file.

    Example:
        >>> save_to_json_file({"key": "value"}, "output.json")
        # Creates a file named "output.json" with the content {"key": "value"}.
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        json.dump(my_obj, myFile)

