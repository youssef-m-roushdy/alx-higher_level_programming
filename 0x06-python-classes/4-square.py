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

    @property
    def size(self):
        """Gets the size of the square.
        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.
        Args:
            value (int): The new size of the square.
        Raises:
            Exception: If value is not an integer or if value is less than 0.
        """
        if type(value) is not int:
            raise Exception("size must be an integer")
        elif value < 0:
            raise Exception("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates and returns the area of the square.
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
