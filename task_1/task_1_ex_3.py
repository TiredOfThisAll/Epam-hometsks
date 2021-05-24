""" Write a Python-script that determines whether the input string is the correct entry for the
'formula' according EBNF syntax (without using regular expressions).
Formula = Number | (Formula Sign Formula)
Sign = '+' | '-'
Number = '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
Input: string
Result: (True / False, The result value / None)

Example,
user_input = '1+2+4-2+5-1' result = (True, 9)
user_input = '123' result = (True, 123)
user_input = 'hello+12' result = (False, None)
user_input = '2++12--3' result = (False, None)
user_input = '' result = (False, None)

Example how to call the script from CLI:
python task_1_ex_3.py 1+5-2

Hint: use argparse module for parsing arguments from CLI
"""
import argparse


def calculate(formula):
    if formula is None:
        return None

    result = 0
    arg_scale = 1
    i = 0

    length = len(formula)
    while i < length:
        start_pos = i
        if not formula[i].isdigit():
            return None
        i += 1

        while i < length and formula[i].isdigit():
            i += 1
        arg = int(formula[start_pos:i])
        result += arg_scale * arg

        if i >= length:
            return result

        if formula[i] == "+":
            arg_scale = 1
        elif formula[i] == "-":
            arg_scale = -1
        else:
            return None
        i += 1
    return None


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("user_input")
    args = parser.parse_args()

    result = calculate(args.user_input)

    print((result is not None, result))


if __name__ == '__main__':
    main()
