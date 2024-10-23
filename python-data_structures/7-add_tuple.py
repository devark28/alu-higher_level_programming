#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    return tuple(
        map(
            lambda x, y: x + y,
            tuple_a + (0, 0),
            tuple_b + (0, 0)
            )
        )
