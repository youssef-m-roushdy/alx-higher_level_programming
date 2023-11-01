#!/usr/bin/python3
def pow(a, b):
    result = 1
    for i in range(0, b):
        if b > 0:
            result *= a
        else:
            result /= a
    return result
