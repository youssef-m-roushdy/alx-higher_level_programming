#!/usr/bin/python3
"""Represent class Square."""


class Square:
    """A class representing a square."""
    def __init__(self, size=0):
        """Initializes a new Square instance with the given size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            Exception: If size is not an integer or if size is less than 0.
        """
        if type(size) is not int:
            raise Exception("size must be an integer")
        elif size < 0:
            raise Exception("size must be >= 0")
        else:
            self.__size = size
