#!/usr/bin/python3
"""Method read_file."""


def read_file(filename=""):
    """Reads and prints the content of a file line by line."""
    with open(filename, mode="r", encoding="utf-8") as myFile:
        read_file = myFile.read()
        print(read_file, end="")
