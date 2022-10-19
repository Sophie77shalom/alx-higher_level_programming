#!/usr/bin/python3
"""Function that prints a square with a character #.
"""


def print_square(size):
    """Method: print a square with #.
    Args:
    size(int): size of the square
    Return:
    No return
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
