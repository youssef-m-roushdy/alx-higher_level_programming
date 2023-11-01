#!/usr/bin/python3
def pow(a, b):
    result = 1
    for i in range(0, b):
        if b > 0:
            result *= a
    for i in range(b, 0):
        if b < 0:
            result /= a
    return result
