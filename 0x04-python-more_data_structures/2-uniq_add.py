#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = []
    for item in my_list:
        if item not in new:
            new.append(item)
    return sum(new)
