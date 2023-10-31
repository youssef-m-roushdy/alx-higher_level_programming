#!/usr/bin/python3
for i in range(0, 100):
    print("{}".format(int(i / 10)) + "{}".format(int(i % 10)), end='')
    if i != 99:
        print(", ", end='')
print("\n")
