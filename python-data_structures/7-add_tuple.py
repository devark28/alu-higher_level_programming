#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    biggest_tuple_len = len(tuple_a) if len(tuple_a) > len(tuple_b) else len(tuple_b)
    for i in range(biggest_tuple_len):
        if i >= len(tuple_a):
            tuple_a += (0,)
        if i >= len(tuple_b):
            tuple_b += (0,)
print(add_tuple((1), (1, 2, 3)))
