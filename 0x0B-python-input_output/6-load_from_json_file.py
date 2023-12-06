#!/usr/bin/python3
"""Method load_from_json_file."""


import json


def load_from_json_file(filename):
    """Loads a Python object from a JSON file."""
    with open(filename, mode="r", encoding="utf-8") as myFile:
        return json.load(myFile)
