#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for key, value in a_dictionary.items():
        print("{:s}: {}".format(key, value*2))
