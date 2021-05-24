"""01-Task1-Task2
Write a Python-script that performs the standard math functions on the data. The name of function and data are
set on the command line when the script is run.
The script should be launched like this:
$ python my_task.py add 1 2

Notes:
Function names must match the standard mathematical, logical and comparison functions from the built-in libraries.
The script must raises all happened exceptions.
For non-mathematical function need to raise NotImplementedError.
Use the argparse module to parse command line arguments. Your implementation shouldn't require entering any
parameters (like -f or --function).
"""

import argparse
import math
import operator


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("operation")
    parser.add_argument("operands", nargs="+")
    args = parser.parse_args()
    if args.operation not in dir(math) and args.operation not in dir(operator):
        raise NotImplementedError
    operands = list(map(float, args.operands))
    operation = getattr(math, args.operation,
                        getattr(operator, args.operation, None))
    result = operation(*operands)
    print(result)


if __name__ == '__main__':
    main()
