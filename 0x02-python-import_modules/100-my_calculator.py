#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]

    if op == '+':
        cal = add(a, b)
    elif op == '-':
        cal = sub(a, b)
    elif op == '*':
        cal = mul(a, b)
    elif op == '/':
        cal = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print(f"{argv[1]} {argv[2]} {b} = {cal}")
