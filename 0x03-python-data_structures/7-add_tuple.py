#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    ext = (0, )
    new = (0, 0)
    if len(tuple_a) or len(tuple_b) < 2:
        tuple_a = tuple_a + ext
        tuple_b = tuple_b + ext
    if len(tuple_a) or len(tuple_b) == 0:
        tuple_a = tuple_a + new
        tuple_b = tuple_b + new
    new_tup = ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))
    return (new_tup)     
