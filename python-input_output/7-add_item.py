#!/usr/bin/python3

''' script that adds all arguments to a Python list'''

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == '__main__':
    args = sys.argv[1:]
    filename = "add_item.json"
    try:
        new = load_from_json_file(filename)
    except Exception:
        new = []
    new.extend(args)
    save_to_json_file(new, filename)
