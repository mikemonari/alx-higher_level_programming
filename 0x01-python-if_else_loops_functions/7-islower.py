#!/usr/bin/python3
def islower(x):

    list1 = []

    for a in range(ord('a'), ord('z') + 1):

        list1.append(chr(a))

    if (x not in list1):

        return True

    else:

        return False
