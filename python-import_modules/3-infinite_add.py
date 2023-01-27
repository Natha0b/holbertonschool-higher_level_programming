#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    argv = argv[1:]
    r = 0

    for a in argv:
        r += int(a)
    print(r)
