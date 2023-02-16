#!/usr/bin/python3
'''import module json'''
import json
'''function that returns an object (Python data structure) '''


def from_json_string(my_str):
    '''returns an object (Python data structure)'''
    return json.loads(my_str)
