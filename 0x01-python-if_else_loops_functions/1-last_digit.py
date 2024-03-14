#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
temp_numb = number

if number < 0:
    number = -1 * number
last_digit = number % 10
if temp_numb < 0:
    last_digit = last_digit * -1

if last_digit > 5:
    print(f"Last digit of {temp_numb} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {temp_numb} is {last_digit} and is zero")
elif (last_digit < 6) and (last_digit != 0):
    print(f"Last digit of {temp_numb} is {last_digit} and is than 6 and not 0")
