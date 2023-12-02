#!/usr/bin/python3
"""Defines a function that adds integers"""


def add_integer(a, b=98):
    """Returns the integer addition value of a and b.

    float arguments are typecasted to integers before addition is done

    Raises:
        TypeError: If either a or b is not integer or float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return(int(a) + int(b))
