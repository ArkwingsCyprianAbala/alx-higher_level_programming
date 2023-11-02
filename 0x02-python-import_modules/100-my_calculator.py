#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    nargs = len(sys.argv) - 1
    if nargs != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    op = sys.argv[2]
    if op != '+' and op != '-' and op != '*' and op != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    from calculator_1 import add, sub, mul, div
    i = int(sys.argv[1])
    j = int(sys.argv[3])

    if op == '+':
        print("{} + {} = {}".format(i, j, add(i, j)))
    elif op == '-':
        print("{} - {} = {}".format(i, j, sub(i, j)))
    elif op == '*':
        print("{} * {} = {}".format(i, j, mul(i, j)))
    else:
        print("{} / {} = {}".format(i, j, div(i, j)))
