#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    updated = {key: value}
    if key not in a_dictionary:
        a_dictionary.update({key:value})
    else:
        for key in a_dictionary:
            if key in updated:
                a_dictionary[key] = updated[key]
    return a_dictionary
