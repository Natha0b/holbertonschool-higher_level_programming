#!/usr/bin/python3
def max_integer(my_list=[]):
    max = my_list[0]

    if my_list == 0:
        return None
    for number in my_list:
        if number > max:
            max = number
    return max
    

