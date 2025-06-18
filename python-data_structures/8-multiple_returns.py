#!/usr/bin/python3
def multiple_returns(sentence):
    if(sentence == ""):
        r_tuple = (len(sentence), None)
    else:
        r_tuple = (len(sentence), sentence[0])
    return r_tuple
