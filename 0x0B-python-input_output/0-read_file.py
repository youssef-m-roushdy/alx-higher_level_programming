#!/usr/bin/python3
"""Method read_file."""


def read_file(filename=""):
    """Reads and prints the content of a file line by line."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            print(content)
    except Exception as e:
        print(f"Error reading the file: {e}")
