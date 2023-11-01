#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        result = number % 10
    else:
        result = -1 * (number % -10)
    print(result, end='')
    return result
