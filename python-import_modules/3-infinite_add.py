#!/usr/bin/python3
from sys import argv
arg = argv[1:]
if __name__ == '__main__':
    r = 0
    for a in arg:
        r += int(a)
    print(r)
