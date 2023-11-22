#!/usr/bin/python3
class Square:
    """A class representing a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size):
            Initializes a new Square instance with the given size.

    Example:
        >>> square = Square(5)
        >>> square.get_size()
        5
    """

    def __init__(self, size):
        """Initializes a new Square instance with the given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
