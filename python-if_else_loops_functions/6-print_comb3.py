#!/usr/bin/python3

for numbers in range(0, 89):
    print("{:02d}".format(numbers), end=', ')
    if numbers == 88:
        print(end=("{}".format("89\n")))