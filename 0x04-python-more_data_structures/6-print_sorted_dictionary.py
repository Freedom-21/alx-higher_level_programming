#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_k = sorted(a_dictionary.keys())
    for k in sorted_k:
        print(f"{k}: {a_dictionary[k]}")
