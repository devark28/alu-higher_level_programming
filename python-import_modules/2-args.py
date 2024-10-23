#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    param_len = len(argv) - 1
    label_str = 'argument' if param_len == 1 else 'arguments'
    label_punct = '.' if param_len == 0 else ':'
    print(f"{param_len} {label_str}{label_punct}")
    for arg in argv[1:]:
        print(f"{argv.index(arg)}: {arg}")
