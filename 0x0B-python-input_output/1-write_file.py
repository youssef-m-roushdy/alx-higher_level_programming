#!/usr/bin/python3
"""Method write_file."""


def write_file(filename="", text=""):
    """Write content inside file."""
    with open(filename, mode="w", encoding="utf-8") as myFile:
        myFile.write(text)
    return len(text)
