#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    tp = tuple(
        map(
            lambda x=0, y=0: x + y,
            tuple_a,
            tuple_b
            )
        )
    return (tp[0], tp[1])
print(add_tuple((1, 2, 3), (1, 2, 3)))
