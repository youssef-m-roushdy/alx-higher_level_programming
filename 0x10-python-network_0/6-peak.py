#!/usr/bin/python3
"""
function that finds a peak in a list of unsorted integers.
"""

def find_peak(list_of_integers):

    if list_of_integers is None or len(list_of_integers) == 0:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[0]

    peak = list_of_integers[0]
    for i in range(1, len(list_of_integers) - 1):
        if list_of_integers[i] > peak:
            peak = list_of_integers[i]
    return peak
        
