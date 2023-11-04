#!/usr/bin/python3
def no_c(my_string):
    newstring = ""
    for elements in my_string:
        if elements != "c" and elements != "C":
            newstring += elements
    return newstring
