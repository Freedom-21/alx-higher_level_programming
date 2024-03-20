#!/usr/bin/python3
def search_replace(my_list, search, replace):
    updated_list = []
    for i in my_list:
        if i == search:
            updated_list.append(replace)
        else:
            updated_list.append(i)
    return updated_list
