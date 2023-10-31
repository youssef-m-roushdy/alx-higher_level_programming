#!/usr/bin/python3
for i in range(0, 99):
    print("{}".format(int(i / 10)) + "{}".format(int(i % 10)), end=', ')
    if i + 1 == 99:
        print("{}".format(int((i + 1) / 10))\
+ "{}".format(int((i + 1) % 10)), end='\n')
