#!/usr/bin/python3

def best_score(a_dictionary):
    best_key = None
    best_value = float('-inf')
    if not a_dictionary:
        return None
    else:
        for key in a_dictionary:
            if a_dictionary[key] > best_value:
                best_value = a_dictionary[key]
                best_key = key
    return best_key
