#!/usr/bin/python3
"""Method  from_json_string."""


import json


def from_json_string(my_str):
    """Parsing string into json format."""
    return json.loads(my_str)
