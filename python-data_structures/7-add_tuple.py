#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    return tuple(
        map(
            lambda x=0, y=0: x + y,
            tuple_a,
            tuple_b
            )
        )
