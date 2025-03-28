#!/usr/bin/python3

import random
number = random.randint(-10000, 10000)

isneg = False
if number < 0:
    number = -number
    isneg = True

lastDig = number % 10
if isneg:
    lastDig = -lastDig
    number = -number

if lastDig > 5:
    print(f"Last digit of {number} is {lastDig} and is greater than 5")
elif lastDig == 0:
    print(f"Last digit of {number} is {lastDig} and is 0")
elif lastDig < 6 and lastDig != 0:
    print(f"Last digit of {number} is {lastDig} and is less than 6 and not 0")
