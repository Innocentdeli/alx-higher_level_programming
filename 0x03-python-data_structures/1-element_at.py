#!/usr/bin/python3
def element_at(my_list, idx):
    if idx in my_list:
        print("Element at index {} is {}".format(idx, my_list[idx]))
    elif idx == -idx:
        print("None")
    elif idx > len(my_list)):
        print("None")
