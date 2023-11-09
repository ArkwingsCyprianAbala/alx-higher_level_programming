#!/usr/bin/python3


def search_replace(my_list, search, replace):
    if my_list is None:
        return
    newlist = my_list[:]
    for idx, c in enumerate(newlist):
        if c == search:
            newlist[idx] = replace
    return newlist
