#!/usr/bin/python3
"""Represent class Square."""


class Square:
    """A class representing a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square instance with the given size and position.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square in a
            2D space.Defaults to (0, 0).

        Raises:
            Exception: If size is not an integer or if size is less than 0.
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if type(size) is not int:
            raise Exception("size must be an integer")
        elif size < 0:
            raise Exception("size must be >= 0")
        else:
            self.__size = size

        if (
            not isinstance(position, tuple) or
            len(position) != 2 or
            not all(isinstance(num, int) for num in position) or
            not all(num >= 0 for num in position)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

    @property
    def position(self):
        """Gets the position of the square.

        Returns:
            tuple: The position of the square in a 2D space.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square.

        Args:
            value (tuple): The new position of the square in a 2D space.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints a square pattern using '#'
        characters and respecting the position."""
        if self.__size == 0:
            print("")
        else:
            for _ in range(0, self.__position[1]):
                print("")
            for _ in range(0, self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
