#!/usr/bin/python3
'''function that writes a string to a text file (UTF8)
    and returns the number of characters written'''


def write_file(filename="", text=""):
    '''writes a string to a text file'''
    with open(filename, 'w') as f:
        number = f.write(text)
        return number
