#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_x = (0, 0)
    tuple_y = (0, 0)
    for i in range(2):
        tuple_x[i] = tuple_a[i] if i < len(tuple_a) else 0
        tuple_y[i] = tuple_b[i] if i < len(tuple_b) else 0
    return tuple(map(sum, zip(tuple_x, tuple_y)))
    
print(add_tuple((1,), (1, 2, 3)))
