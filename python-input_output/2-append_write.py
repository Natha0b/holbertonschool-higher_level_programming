#!/usr/bin/python3
'''function that appends a string at the end of a text file
    (UTF8) and returns the number of characters added'''


def append_write(filename="", text=""):
    '''that appends a string at the end of a text file'''
    with open(filename, 'a') as f:
        number = f.write(text)
        return number
