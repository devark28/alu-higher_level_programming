#!/usr/bin/python3


def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    result = 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
    char_arr = [c for c in roman_string]
    for i in range(1, len(char_arr)):
        prev_i = i - 1
        max_i = max(char_arr[prev_i:i+1], key=lambda x: roman_dict[x])
        if max_i == char_arr[prev_i]:
            result += roman_dict[char_arr[prev_i]]
        else:
            result -= roman_dict[char_arr[prev_i]]
    result += roman_dict[char_arr[-1]]
    return result
# print(roman_to_int(None))
