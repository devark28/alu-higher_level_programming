#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    tp = tuple(
        map(
            lambda x=0, y=0: x + y,
            tuple_a,
            tuple_b
            )
        )
    return (tp[0] if tp.__len__() > 0 else 0,
            tp[1] if tp.__len__() > 1 else 0)
print(add_tuple((1), (1, 2, 3)))
