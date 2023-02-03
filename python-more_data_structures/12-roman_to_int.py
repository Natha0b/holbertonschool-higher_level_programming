#!/usr/bin/python3
def roman_to_int(roman_string):

    roman_numbers = {
        'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1
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
