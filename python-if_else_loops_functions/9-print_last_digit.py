#!/usr/bin/python3


def print_last_digit(number):
    positive = abs(number)
    last_digit = positive % 10
    print(f"{last_digit:d}", end="")
    return last_digit
