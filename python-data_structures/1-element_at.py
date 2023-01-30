#!/usr/bin/python3
def element_at(my_list, idx):

    if idx < 0:
        return None
    if idx > (len(my_list)):
        print("Element at index {:d} is {}".format(idx, my_list))
    else:
        return None
