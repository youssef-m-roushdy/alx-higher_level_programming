#!/usr/bin/python3
"""Method append_write."""


def append_write(filename="", text=""):
    """Apend content inside file."""
    with open(filename, mode="a", encoding="utf-8") as myFile:
        myFile.write(text)
    return len(text)
