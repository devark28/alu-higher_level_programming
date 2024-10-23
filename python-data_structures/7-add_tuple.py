#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    # biggest_tuple_len = len(tuple_a) if len(tuple_a) > len(tuple_b) else len(tuple_b)
    # biggest_tuple_len = biggest_tuple_len if biggest_tuple_len <= 2 else 2
    # tuple_c = tuple()
    # for i in range(2):
    #     tuple_c[i] = tuple_a[i] if i < len(tuple_a) else 0
    return list(map(sum, zip(tuple_a, tuple_b)))
    
print(add_tuple((1), (1, 2, 3)))
