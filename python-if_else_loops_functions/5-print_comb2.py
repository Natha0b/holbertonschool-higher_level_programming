#!/usr/bin/python3

for numbers in range(0, 99):
    print("{:02d}".format(numbers), end=', ')
    if numbers == 98:
        print(end=("{}".format("99\n")))
   
