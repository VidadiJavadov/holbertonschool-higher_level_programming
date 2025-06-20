#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        new_list = my_list[:x]
        return new_list
    except:
        print("stack overflow")
