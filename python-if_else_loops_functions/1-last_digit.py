#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Calculate the last digit based on the problem's specific definition for negative numbers
if number < 0:
    last_digit = -(abs(number) % 10)
else:
    last_digit = number % 10

# Split the f-string to adhere to the 79-character limit
output = (
    f"Last digit of {number} is {last_digit}"
)

if last_digit > 5:
    output += " and is greater than 5"
elif last_digit == 0:
    output += " and is 0"
else:  # last_digit < 6 and not 0
    output += " and is less than 6 and not 0"

print(output)
