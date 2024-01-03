#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
#converting number to string
str_number = str(number)
#slicing last digit of number
int_number = int(number[-1])
if int_number > 5:
    print(f"The Last digit of {number} is {int_number} and is greater than 5")
elif int_number == 0:
    print(f"The Last digit of {number} is {int_number} and is 0")
elif int_number < 6 and int_number > 0:
    print(f"The Last digit of {number} is {int_number} and is less than 6 and not 0"}
