#!/usr/bin/python3
def roman_to_int(roman_string):

    roman_numbers = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
    i = 0
    num = 0
    while i < len(roman_string):
        if i + 1 < len(roman_string)and roman_string[i:i + 2]in roman_numbers:
            num += roman_numbers[roman_string[i:i + 2]]
            i += 2
        else:
            num += roman_numbers[roman_string[i]]
            i += 1
    return num
