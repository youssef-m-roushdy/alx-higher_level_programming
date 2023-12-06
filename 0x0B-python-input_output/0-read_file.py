#!/usr/bin/python3
"""Reads and prints the content of a file line by line."""


def read_file(filename=""):
    """Reads and prints the content of a file line by line."""
    with open("my_file_0.txt", mode="r", encoding="utf-8") as myFile:
        for line in myFile:
            print(line, end="")
