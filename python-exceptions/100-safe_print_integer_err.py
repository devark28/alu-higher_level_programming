#!/usr/bin/python3
from sys import stderr

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value), end="")
        return True
    except Exception as e:
        stderr.write("Exception: {}".format(e))
        return False
    finally:
        print()
