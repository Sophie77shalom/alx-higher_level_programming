#!/usr/bin/python3
"""Function that adds two integers.

"""





def add_integer(a, b=98):

    """Method: addition of a and b.

    Args:

    a(int, float): first number

    b(int, float): second number

    Returns:

    The addition of a and b

    """



    if not isinstance(a, (int, float)):

        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):

        raise TypeError("b must be an integer")

    return (int(a) + int(b))
