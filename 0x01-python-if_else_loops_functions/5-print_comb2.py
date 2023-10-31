#!/usr/bin/python3
for i in range(0, 100):
    print(f"{int(i / 10)}{int(i % 10)}", end='')
    if i != 99:
        print(", ", end='')

