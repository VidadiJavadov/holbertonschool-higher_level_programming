#!/bin/bash/python3

def print_last_digit(number):
    result = 0
    if(number > 0):
        result = number % 10
    elif(number < 0):
        result = -(abs(number) % 10)

    return result
