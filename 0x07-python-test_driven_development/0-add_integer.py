#!/usr/bin/python3
"""Defines a function that adds two integers."""


def add_integer(a, b=98):
    """Returns the integer addition of a and b.
    a and b must be first casted to integers if they are floats.
    Raises:
        TypeError: if either a or b is not an integer or float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
