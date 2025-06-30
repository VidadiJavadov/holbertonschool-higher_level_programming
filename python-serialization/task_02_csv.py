#!/usr/bin/python3
import csv
import json

def convert_csv_to_json(filename):
    with open("data.json", mode="w") as file:
        try:
            csv_data = csv.DictReader(file)
            json.dump(csv_data, "data.json")
            return True
        except FileNotFoundError:
            print("file not found")
            return False
