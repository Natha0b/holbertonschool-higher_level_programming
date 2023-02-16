#!/usr/bin/python3
'''import module json'''
import json
'''function that creates an Object from a “JSON file”'''


def load_from_json_file(filename):
    ''' creates an Object from a “JSON file”'''
    with open(filename, "r") as f:
        return json.load(f)
