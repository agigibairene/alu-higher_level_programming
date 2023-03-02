#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    total_a = len(tuple_a)
    total_b = len(tuple_b)
    if total_a == 0:
        tuple_a = (0,0)
    elif total_a == 1:
        tuple_a = (tuple_a[0],0)
    if total_b < 1:
        tuple_b = (0,0)
    elif total_b < 2:
        tuple_b = (tuple_b[0],0)

    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
