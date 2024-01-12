#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_list = list(set(my_list))
    list_add = 0
    for i in new_list:
        list_add += i
    return list_add
