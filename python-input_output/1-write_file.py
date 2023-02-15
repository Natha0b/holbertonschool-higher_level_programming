#!/usr/bin/python3
'''function that reads a text file (UTF8) and prints it to stdout'''


def write_file(filename="", text=""):
    '''that reads a text file '''
    with open(filename, 'w') as f:
        number = f.write(text)
        return number
