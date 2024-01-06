#!/usr/bin/python3
def no_c(my_string):
    for i in my_string:
        count = 0
        if i == "c" or i == "C":
            my_string.remove(count, i)
            count += 1
    return my_string
