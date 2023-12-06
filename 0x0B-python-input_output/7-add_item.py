#!/usr/bin/python3
"""Main script to add arguments to a Python list and save to a JSON file."""


import sys
from os import path
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    """Main function."""
    # Get command line arguments (excluding the script name)
    argv = sys.argv[1:]

    # Initialize an empty list if the file doesn't exist
    if not path.exists("add_item.json"):
        save_to_json_file([], "add_item.json")

    # Load existing data from the file
    loaded_data = load_from_json_file("add_item.json")

    # Add new items to the list
    loaded_data.extend(argv)

    # Save the updated list to the file
    save_to_json_file(loaded_data, "add_item.json")
