#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":
    param_len = len(argv) - 1
    if param_len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    result = None
    match argv[2]:
        case '+':
            add(a, b)
        case '-':
            sub(a, b)
        case '*':
            mul(a, b)
        case '/':
            div(a, b)
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    print(f"{a} {op} {b} = {result}")
