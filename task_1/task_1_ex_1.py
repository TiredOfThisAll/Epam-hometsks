import argparse


dictionary = {
    "+": lambda operand_1, operand_2: operand_1 + operand_2,
    "-": lambda operand_1, operand_2: operand_1 - operand_2,
    "*": lambda operand_1, operand_2: operand_1 * operand_2,
    "/": lambda operand_1, operand_2: operand_1 / operand_2,
}


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("operand_1")
    parser.add_argument("operation")
    parser.add_argument("operand_2")
    args = parser.parse_args()

    if args.operation not in dictionary:
        raise NotImplementedError()
    print(dictionary[args.operation](float(args.operand_1), float(args.operand_2)))


if __name__ == '__main__':
    main()
