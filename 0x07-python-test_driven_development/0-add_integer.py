#!/usr/bin/python3
def add_integer(a, b=98):
    if type(a) not in [int, float]:
        raise Exception("a must be an integer")
    elif type(b) not in [int, float]:
        raise Exception("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
