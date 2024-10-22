#!/usr/bin/python3


def print_last_digit(number):
    positive = abs(number)
    last_digit = positive % 10
    print("{last_digit:d}")
    return last_digit

print_last_digit(98)
