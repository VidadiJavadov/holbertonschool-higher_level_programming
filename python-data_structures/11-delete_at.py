#!/usr/bin/python3
"""
A module with a function that deletes an element from a list.
"""


def delete_at(my_list=[], idx=0):
    """Deletes the item at a specific position in a list.

    Args:
        my_list: The list to be modified.
        idx: The index of the element to delete.

    Returns:
        The modified list, or the original if the index is out of range.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
