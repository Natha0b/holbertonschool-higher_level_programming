#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list[:]
    for idx in range(len(my_list)):
        if search == new[idx]:
            new[idx] = replace
    return new
