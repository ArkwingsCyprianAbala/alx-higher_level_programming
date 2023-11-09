#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    romand = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    romann = 0
    for i in range(len(roman_string)):
        if i > 0 and romand[roman_string[i]] > romand[roman_string[i - 1]]:
            romann += romand[roman_string[i]] - 2 * \
                        romand[roman_string[i - 1]]
        else:
            romann += romand[roman_string[i]]
    return romann
