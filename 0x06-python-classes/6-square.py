#!/usr/bin/python3
"""Represent class Square."""


class Square:
    """A class representing a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square instance with the given size and position.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square in a
            2D space. Defaults to (0, 0).

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

        if position[0] >= 0 and position[1] >= 0:
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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
        if value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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
            for j in range(0, self.__position[1]):
                print("")
            for i in range(0, self.__size):
                for k in range(0, self.__position[0]):
                    print(" ", end="")
                for m in range(0, self.__size):
                    print("#", end="")
                print("")
