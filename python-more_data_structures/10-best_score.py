#!/usr/bin/python3

def best_score(a_dictionary):
    best_score = a_dictionary[0]
    if not a_dictionary:
        return None
    else:
        for key in a_dictionary:
            if(a_dictionary[key] > best_key):
                best_key = a_dictionary[key]
    return best_key
