#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_key = None
    for key in a_dictionary:
        if best_key is None or a_dictionary[key] > a_dictionary[best_key]:
            best_key = key
    return best_key
