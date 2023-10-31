#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = -98
if number > 0:
    lastD = number % 10
elif number < 0:
    lastD = number % (-10)
if 0 < lastD < 6:
    print(f"Last digit of {number} is {lastD} and is less than 6 and not 0")
elif lastD == 0:
    print(f"Last digit of {number} is {last} and is 0")
elif lastD > 5:
    print(f"Last digit of {number} is {lastD} and is greater than 5")
