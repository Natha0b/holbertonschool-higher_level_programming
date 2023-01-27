#!/usr/bin/python3
from sys import argv
argv = argv[1:]
if __name__ == '__main__':
    r = 0
    for a in argv:
        r += int(a)
    print(r)
