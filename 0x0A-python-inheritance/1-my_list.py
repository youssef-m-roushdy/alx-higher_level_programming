#!/usr/bin/python3
"""A custom list class that extends the built-in list class."""


class MyList(list):
    """A custom list class that extends the built-in list class.

    This class adds a method to print the sorted elements of the list.

    Attributes:
        Inherits attributes from the built-in list class.

    Methods:
        print_sorted(): Prints the sorted elements of the list.

    Raises:
        TypeError: If the list contains elements that are not integers.
    """

    def print_sorted(self):
        """Prints the sorted elements of the list."""
        sorted_list = sorted(self[:])
        print(sorted_list)
