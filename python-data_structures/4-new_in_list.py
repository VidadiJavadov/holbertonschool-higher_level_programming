#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces an element in a copy of a list at a specific position."""
    list_copy = my_list.copy()
    if idx < 0 or idx >= len(list_copy):
        return list_copy
    list_copy[idx] = element
    return list_copy
