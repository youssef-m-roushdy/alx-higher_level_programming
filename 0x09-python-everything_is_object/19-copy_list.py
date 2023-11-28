#!/usr/bin/python3
"""Creates a shallow copy of the input list."""


def copy_list(l):
    """
    Creates a shallow copy of the input list.

    Parameters:
    - l (list): The input list to be copied.

    Returns:
    list: A new list that is a shallow copy of the input list.

    Example:
    >>> original_list = [1, 2, 3]
    >>> copied_list = copy_list(original_list)
    >>> print(copied_list)
    [1, 2, 3]
    """
    return l[:]
