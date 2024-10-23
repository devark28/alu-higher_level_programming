#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    param_len = len(argv) - 1
    print(f"{param_len} {'argument' if param_len == 1 else 'arguments'}{'.' if param_len == 0 else ':'}")
    for arg in argv[1:]:
        print(f"{argv.index(arg)}: {arg}")
