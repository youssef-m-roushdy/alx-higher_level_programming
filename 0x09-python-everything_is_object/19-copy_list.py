#!/usr/bin/python3

def copy_list(list):
    """
    Creates a shallow copy of the input list.

    Parameters:
    - list (list): The input list to be copied.

    Returns:
    list: A new list that is a shallow copy of the input list.

    Example:
    >>> original_list = [1, 2, 3]
    >>> copied_list = copy_list(original_list)
    >>> print(copied_list)
    [1, 2, 3]
    """
    new_list = list[:]
    return new_list
