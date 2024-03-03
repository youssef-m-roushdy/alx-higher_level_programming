#!/usr/bin/python3
"""
function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
    list_of_integers (list): A list of unsorted integers.

    Returns:
    int: The peak integer.
    """
    # Check if the list is empty
    if not list_of_integers:
        return None

    # Initialize the peak variable
    peak = list_of_integers[0]

    # Iterate through the list to find the peak
    for i in range(1, len(list_of_integers)):
        if list_of_integers[i] > peak:
            peak = list_of_integers[i]

    return peak
