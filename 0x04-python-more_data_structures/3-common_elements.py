#!/usr/bin/python3
def common_elements(set_1, set_2):
    new = []
    for e in set_1:
        for i in set_2:
            if e == i:
                new.append(i)
    return new
