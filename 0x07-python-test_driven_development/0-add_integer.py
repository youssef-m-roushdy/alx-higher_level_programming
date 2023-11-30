#!/usr/bin/python3
"""Module for add_integer method."""


def add_integer(a, b=98):
    """
    Adds two numbers.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If either a or b is not an integer or float.

    Examples:
        >>> add_integer(2, 3)
        5
        >>> add_integer(2.5, 3.5)
        5
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
