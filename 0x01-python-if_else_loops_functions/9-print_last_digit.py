#!/usr/bin/python3
def print_last_digit(number):
    new = (number % 10)
    print("{:d}".format(new, end=''))
