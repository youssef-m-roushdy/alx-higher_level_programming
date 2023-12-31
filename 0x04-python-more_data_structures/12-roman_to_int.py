#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0
    r_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    prev_value, total = 0, 0
    for numeral in roman_string[::-1]:
        value = r_n[numeral]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total
