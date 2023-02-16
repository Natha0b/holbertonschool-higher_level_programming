#!/usr/bin/python3

''' script that adds all arguments to a Python list'''

import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == '__main__':
    args = sys.argv[1:]
    filename = "add_item.json"
    try:
        file = load_from_json_file(filename)
    except FileNotFoundError:
        file = []
    file.extend(args)
    save_to_json_file(file, filename)
