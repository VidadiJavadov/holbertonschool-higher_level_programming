#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    del a_dictionary["{}".format(key)]
    return a_dictionary
