#!/usr/bin/python3

def max_integer(my_list=[]):

    length = len(my_list)
    if length == 0:
        return None

    maximum = 0
    for i in range(0, length):
        if my_list[i] > maximum:
            maximum = my_list[i]

    return maximum
