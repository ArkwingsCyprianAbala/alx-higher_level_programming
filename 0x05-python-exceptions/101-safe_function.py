#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        numbr = fct(*args)
        return numbr
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None
