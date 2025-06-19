#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    a_dictionary["{}".format(key)] = "{}".format(value)
    return a_dictionary
