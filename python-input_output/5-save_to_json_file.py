#!/usr/bin/python3
'''import module json'''
import json
'''function that writes an Object to a text file, using a JSON'''


def save_to_json_file(my_obj, filename):
    '''writes an Object to a text file, using a JSON'''
    with open(filename, 'w') as f:
        return json.dump(my_obj, f)
