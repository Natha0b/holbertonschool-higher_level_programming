#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":

    args = len(argv) - 1
    if args == 0:
        print("0 arguments.")
    else:
        if args == 1:
            print("{:d} argument:".format(args))
        else:
            print("{:d} arguments:".format(args))
        for i, args in enumerate(argv[1:]):
            print("{:d}: {}".format(i + 1, args))
