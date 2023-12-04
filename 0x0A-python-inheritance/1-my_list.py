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
        """Prints the elements of the list in sorted order.

        This method checks if all elements in the list are integers, raises a
        TypeError if not, and then prints the sorted elements of the list.

        Raises:
        TypeError: If the list contains elements that are not integers.
        """
        for ele in self:
            if type(ele) != int:
                raise TypeError("The list must be list of integers")
        self.sort()
        print(self)
