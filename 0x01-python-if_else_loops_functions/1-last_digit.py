#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if number < 0:
    last_digit = -last_digit
if last_digit > 5:
    message = "greater than 5"
elif last_digit == 0:
    message = "0"
else:
    message = "less than 6 and not 0"

print(f"The last digit of {number} is {last_digit} and it's {message}.")
