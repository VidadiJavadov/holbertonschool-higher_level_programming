#!/usr/bin/python3
"""This is a list to json"""
import json
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

try:
    myList = load_from_json_file(filename)
except:
    myList = []

myList.extend(sys.argv[1:])
save_to_json_file(myList)
