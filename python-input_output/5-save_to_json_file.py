#!/usr/bin/python3
'''import module json'''
import json
'''function that returns the JSON representation of an object'''


def save_to_json_file(my_obj, filename):
    '''returns the JSON representation of an object '''
    with open(filename, 'w') as f:
        return json.dump(my_obj, f)
