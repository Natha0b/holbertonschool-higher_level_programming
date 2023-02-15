#!/usr/bin/python3
'''function that reads a text file (UTF8) and prints it to stdout'''


def read_file(filename=""):
    '''that reads a text file '''
    with open(filename) as f:
        for line in f:
            print(line, end='')
