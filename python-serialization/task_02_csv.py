#!/usr/bin/python3
import csv
import json

def convert_csv_to_json(filename):
    with open("data.json", mode="w") as file:
        try:
            with open(filename, mode="r", newline='') as csvfile:
                csv_data = csv.DictReader(csvfile)
                json.dump(list(csv_data), file)
            return True
        except FileNotFoundError:
            print("file not found")
            return False
