#!/usr/bin/python3
"""
A module for tuple manipulation.
"""


def add_tuple(tuple_a=(), tuple_b=()):
    """Adds two tuples element-wise.

    Pads tuples with 0s if they have fewer than two elements.
    Uses only the first two elements if they are longer.

    Args:
        tuple_a: The first tuple.
        tuple_b: The second tuple.

    Returns:
        A new tuple containing the sum of the first two
        elements of each input tuple.
    """
    padded_a = tuple_a + (0, 0)
    padded_b = tuple_b + (0, 0)

    result_tuple = (padded_a[0] + padded_b[0], padded_a[1] + padded_b[1])
    return result_tuple
