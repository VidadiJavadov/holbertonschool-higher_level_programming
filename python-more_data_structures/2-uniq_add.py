#!/usr/bin/python3

def uniq_add(my_list=[]):
    result = 0
    unique_list = set(my_list)
    for i in unique_list:
        result += i
    return result
