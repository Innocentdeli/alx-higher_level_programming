#!/usr/bin/python3

def best_score(a_dictionary):
    Max = 0
    key = ''
    if not a_dictionary:
        return None
    for x, y in a_dictionary.items():
        if y > Max:
            Max = y
            key = x
    return key
