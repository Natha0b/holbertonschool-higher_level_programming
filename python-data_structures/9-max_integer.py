#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max = my_list[0]
        for number in my_list:
            if number > max:
                max = number
        return max
    return None
