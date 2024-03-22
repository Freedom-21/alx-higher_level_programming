#!/usr/bin/python3
def best_score(a_dictionary):
    best_score = 0
    best_scorer = None
    if a_dictionary is not None:
        for k, v in a_dictionary.items():
            if v > best_score:
                best_score = v
                best_scorer = k
    return best_scorer
