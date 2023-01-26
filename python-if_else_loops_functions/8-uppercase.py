#!/usr/bin/python3
def uppercase(str):
    i = ""
    for string in str:
        if ((ord(string) >= 97 and ord(string) <= 123)):
            change = ord(string) - 32
            i += chr(change)
        else:
            change = string
            i += change
    print("{}".format(i))
